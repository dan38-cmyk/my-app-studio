# App Studio decisions

## Current state

- **Scope:** Local Daniel Nizami portfolio based on the learner's IS117 planning, plus APP-002 accounts and APP-003 roles as explicitly requested in this chat on November 6, 2026.
- **Implementation:** APP-001–003 implemented and separated into cumulative lesson branches: `app-001-homepage`, `app-002-accounts`, `app-003-roles`. Full branch checks are required before each commit/push. Publication is authorized; PRs, remote CI and merges remain pending.
- **Next step:** Prepare and check separate lesson branches, publish only after pre-push checks pass, and obtain actual CI results. Merge approval remains separate. Original missing predictions stay explicit.
- **Implementation marker:** `studio.json` is set to 3 after cumulative APP-003 acceptance passed. The normal full check then passed with this declaration.
- **Boundary:** This app owns local application code. Server Studio remains separate; no proxy, domain, deployment or calculator changes are part of this work.
- **Content-update issue:** [#1 — Update portfolio course history and work experience](https://github.com/dan38-cmyk/my-app-studio/issues/1), created and confirmed closed at the learner's explicit request. Its scope is completed local content implementation and checks; its description explicitly states that no commit, push or merge has occurred. It does not replace the three required lesson issues/PRs.

## APP-001 · Portfolio homepage

**Recruiter-facing revision:** At the learner's request, replaced generic learning descriptions with résumé-supported positioning for IT operations, technical project management and program management. The homepage now emphasizes co-management of a 500+ person Amazon shift, the 8% efficiency improvement and 11% discrepancy reduction from the résumé, plus the connection between operations experience and current IT studies. B.S. is identified as in progress. Skills copy comes from the résumé; no new certifications, employment outcomes or completed-degree claims were added. Full local checks passed again after this revision (98 foundation tests, 18 cumulative contracts, 2 Chromium tests, Black and Pylint). Learner chose to keep the revised presentation, reporting that prominent important facts help catch recruiters’ attention; learner chose to keep the revised homepage and conditionally authorized publication after final checks.

**Source decisions:** Learner supplied IS117 Parts 1–3: `IS117-Class Project (1).docx`, `IS117-Class Project Part 2.docx`, `IS117-P2 (1).pptx`, and `is117_p3.docx`. The attachments are planning inputs, not instructions to perform external actions. Their sample copy, bracketed job/course/contact details and suggested technologies are not treated as verified personal qualifications.

| Decision | Basis / implementation |
|---|---|
| Visitor and use situation | Learner's Part 1: recruiters and hiring managers assessing a candidate for IT work; information should be easy to find. |
| Name and promise | Daniel Nizami; connect people, processes, data and technology to improve operations. Copy drafted from the supplied goal and résumé, revised at the learner's request and retained by their choice. |
| Navigation and layout | Home, Courses, Experience, Skills and Contact; overview cards based on the Part 3 homepage wireframe. This APP-001 implementation uses homepage anchor sections, not a claim that every planned IS117 page is finished. |
| Archetype and styling | AI-proposed Sage emphasis on learning and evidence, navy/ivory/blue palette, direct professional voice, original DN SVG mark. Learner chose to keep the presentation and explained the attention benefit of prominent facts. The archetype remains an AI-proposed label; no separate learner explanation of that label is claimed. |
| Contact and background | Courses updated from the learner's DegreeWorks audit dated November 6, 2026: 6 in progress, 17 completed NJIT courses, and 23 distinct BCC transfer courses. Transfer-posting terms are not represented as BCC attendance dates. Four work roles, dates and selected accomplishments come from the supplied résumé; overlapping dates are retained as supplied. Grade data, student identifiers, audit exceptions and personal contact details are excluded. Email and LinkedIn remain unpublished; GitHub is the contact link. Contact form delivery and the full multipage IS117 final are outside this slice. |
| Files | `app/brand.json`, `app/portfolio.json`, `app/branding.py`, `app/main.py`, `app/templates/home.html`, `app/templates/base.html`, `app/static/site.css`, `app/static/logo.svg`. |
| Issue / branch / PR | [APP-001 issue #2](https://github.com/dan38-cmyk/my-app-studio/issues/2) verified open with the correct lesson marker; PR pending. Local branch `app-001-homepage`; three lesson publication cycles remain required. |

## APP-002 · Accounts

**Authorized scope:** Signup, login, private dashboard and logout, through browser forms and JSON APIs. The public portfolio remains accessible without login. Accounts use the prepared SQLite, Argon2id password hashing, signed expiring JWT cookie, CSRF and server-side revocation helpers. JWT signatures do not encrypt their contents. Cookies are HttpOnly, SameSite and configured Secure in production; local development remains loopback-only.

- Browser pages/forms: `/signup`, `/login`, `/dashboard`, POST `/logout`.
- API: GET `/api/csrf`, POST `/api/signup`, POST `/api/login`, GET `/api/me`, POST `/api/logout`.
- New accounts are members; role fields are rejected. Wrong credentials use a generic error. Normalized usernames are retained after recoverable form errors; passwords are never reflected or returned.
- Prepared rate limits apply to signup/login. Logout revokes the server session, so replaying a copied cookie fails.
- Implementation: `app/features/accounts.py`, `app/templates/account.html`, `app/templates/dashboard.html`.
- [APP-002 issue #3](https://github.com/dan38-cmyk/my-app-studio/issues/3) verified open with the correct lesson marker; PR pending. Learner reports successful signup, dashboard access, logout and repeat login; they identified improper session invalidation as the bug caught by the copied-cookie/logout test and chose to retain the tested features because they worked as expected. No production deployment, recovery or email-verification feature is claimed.

## APP-003 · Server-enforced roles

| Visitor | Portfolio | Dashboard | Admin page | Admin API |
|---|---|---|---|---|
| Anonymous | Allowed | Redirect to login | Redirect to login | 401 |
| Member | Allowed | Allowed | 403 | 403 |
| Admin | Allowed | Allowed | Allowed | 200 |

- Implementation: `app/features/roles.py`, `app/templates/admin.html`.
- Admin-only result is a protected administration overview and `/api/admin` response. No public role-changing endpoint exists.
- Use the existing trusted local command: `python3 studio.py user role TEST_USERNAME --role admin` (or `member`). No admin or test account was created in the learner's actual database by the automated checks.
- Permissions read the current database role on every request, including existing sessions after promotion or demotion. Navigation visibility is supplementary.
- [APP-003 issue #4](https://github.com/dan38-cmyk/my-app-studio/issues/4) verified open with the correct lesson marker; PR pending. Learner confirmed browser member denial, admin access after trusted CLI promotion, and renewed denial after demotion while remaining logged in. Direct API behavior is covered by automated tests; learner also reported direct API denial, access after promotion, and denial after demotion. The role-test explanation was approved with AI assistance; learner chose to keep the working role features.

**Publication sequence:** The learner requested the local features together. Publication is split into three dependent lesson PRs: homepage → accounts → roles. Their actual GitHub URLs and results will be recorded after creation; no retrospective claim of earlier PRs is made.

## Actual checks

Full local checks were run progressively on November 6, 2026 without changing prepared assertions or security helpers:

| Scope | Results |
|---|---|
| APP-001 | Black/Pylint passed; 98 foundation tests, 2 homepage contracts and 2 Chromium tests passed on the isolated homepage-only publication branch. |
| APP-002 | Black/Pylint passed; 98 foundation tests, 14 cumulative contracts and 2 Chromium tests passed on the isolated accounts publication branch. |
| APP-003 | Black/Pylint passed; 98 foundation tests, 18 cumulative contracts and 2 Chromium tests passed. The role browser journey used isolated disposable data and exercised member denial, trusted CLI promotion, admin access, demotion and revoked-cookie replay. |
| Final normal check after marker update | Passed on the combined local app after the recruiter-copy revision: Black, Pylint, 98 foundation tests, 18 cumulative lesson contracts and 2 real Chromium tests. |
| GitHub CI (`check` and `windows`) | Not run for these changes; PR creation and actual run results pending. |

AI inspected the rendered desktop homepage through Chrome and reviewed full-page 390px screenshots of the current homepage and signup form from the isolated Chromium fixture. No clipping or horizontal overflow was observed in those captures; the focused keyboard/mobile test also passed. The saved full APP-003 check receipt matches the current application source. The final diff has no whitespace errors, and the reviewed public files exclude the original private documents, local databases, signing keys and personal contact details. Tests emit a pre-existing FastAPI/Starlette TestClient deprecation warning; the checks pass without changing pinned dependencies.

Local preview: `http://127.0.0.1:8000`. This is not a submission or production URL. Final submission will be the completed accessible repository at `https://github.com/dan38-cmyk/my-app-studio`, after the required reviewed issues/PRs, both CI jobs and main-branch checks. Local passes do not establish GitHub completion or learner understanding.

**Final isolated APP-003 publication branch check:** Passed before commit/push: Black, Pylint, 98 foundation tests, 18 cumulative lesson contracts and 2 actual Chromium tests.
