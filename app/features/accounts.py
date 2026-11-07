"""Browser forms and JSON endpoints share the prepared account protections."""

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, PublicUser, SignupInput

router = APIRouter()


def page(request, template, *, status=200, **context):
    """Render a page with a session-bound CSRF field and any new session cookie."""
    cookies = Response()
    token = security.csrf_token(request, cookies)
    response = request.app.state.templates.TemplateResponse(
        request=request,
        name=template,
        context={"csrf_token": token, **context},
        status_code=status,
    )
    response.raw_headers.extend(
        (key, value) for key, value in cookies.raw_headers if key == b"set-cookie"
    )
    return response


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Issue a token through the same origin without exposing the session cookie."""
    return {"csrf_token": security.csrf_token(request, response)}


@router.post("/api/signup", response_model=PublicUser, status_code=201)
def api_signup(request: Request, credentials: SignupInput):
    """Create only a member, after CSRF and rate-limit checks."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings, credentials.username, credentials.password
    )


@router.post("/api/login", response_model=PublicUser)
def api_login(request: Request, response: Response, credentials: LoginInput):
    """Sign in with a protected cookie, never a token in the JSON body."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    return security.login(request, response, credentials.username, credentials.password)


@router.get("/api/me", response_model=PublicUser)
def api_me(user: dict = Depends(security.require_user)):
    """Filter private session fields out of the authenticated identity."""
    return user


@router.post("/api/logout")
def api_logout(request: Request, response: Response):
    """Revoke the session on the server as well as deleting the browser cookie."""
    security.require_user(request)
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.logout(request, response)
    return {"message": "Logged out."}


@router.get("/signup", include_in_schema=False)
def signup_form(request: Request):
    """Show a usable local signup form."""
    return page(request, "account.html", action="signup", username="", error=None)


@router.get("/login", include_in_schema=False)
def login_form(request: Request):
    """Offer login without exposing existing credentials."""
    return page(request, "account.html", action="login", username="", error=None)


async def submit_form(request, action):
    """Keep validated usernames after errors; never reflect passwords or tokens."""
    username = ""
    try:
        async with request.form(max_fields=3, max_files=0) as form:
            security.require_csrf(request, form.get("csrf_token"))
            schema = SignupInput if action == "signup" else LoginInput
            fields = {key: value for key, value in form.items() if key != "csrf_token"}
            credentials = schema.model_validate(fields)
        username = credentials.username
        response = RedirectResponse(
            "/login?created=1" if action == "signup" else "/dashboard", status_code=303
        )
        if action == "signup":
            security.limit_signup(request)
            security.signup(request.app.state.settings, username, credentials.password)
        else:
            security.login(request, response, username, credentials.password)
        return response
    except ValidationError:
        status, message, headers = (
            422,
            "Check your username and password against the requirements below.",
            {},
        )
    except HTTPException as error:
        status, message, headers = error.status_code, error.detail, error.headers or {}
    response = page(
        request,
        "account.html",
        status=status,
        action=action,
        username=username,
        error=message,
    )
    response.headers.update(headers)
    return response


@router.post("/signup", include_in_schema=False)
async def signup_submit(request: Request):
    """Handle signup through the same guards used by the JSON API."""
    return await submit_form(request, "signup")


@router.post("/login", include_in_schema=False)
async def login_submit(request: Request):
    """Handle a browser login, including generic wrong-credential errors."""
    return await submit_form(request, "login")


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    """Protect the private page on the server, including direct navigation."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    return page(request, "dashboard.html", user=user)


@router.post("/logout", include_in_schema=False)
async def logout_submit(request: Request):
    """Require a POST and valid CSRF before revoking a browser session."""
    async with request.form(max_fields=1, max_files=0) as form:
        security.require_csrf(request, form.get("csrf_token"))
    response = RedirectResponse("/login", status_code=303)
    security.logout(request, response)
    return response
