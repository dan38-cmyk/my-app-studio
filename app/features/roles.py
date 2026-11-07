"""Current server-side roles protect both HTML and API administration."""

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from app import security

router = APIRouter()


@router.get("/api/admin")
def admin_api(user: dict = Depends(security.require_admin)):
    """Require a live session and the current database admin role on every call."""
    return {"message": "Administration access granted.", "username": user["username"]}


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request):
    """A typed URL receives the same permission boundary as navigation."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    allowed = user["role"] == "admin"
    return request.app.state.templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"allowed": allowed, "user": user},
        status_code=200 if allowed else 403,
    )
