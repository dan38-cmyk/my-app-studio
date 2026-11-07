# App Studio decisions

## Current state

- **Current feature:** APP-001.
- **Branch:** `app-001-homepage`.
- **Scope:** Recruiter-facing Daniel Nizami homepage from IS117 planning, supplied course history and résumé.
- **Boundary:** Accounts and roles are excluded from this branch. The learner requested all local features together; their publication is separated into one PR per lesson. No server/deployment changes.
- **Next step:** Full checks, PR review and both CI jobs. Merge approval has not been given.

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

## Actual evidence

- Own lesson issue: [#2](https://github.com/dan38-cmyk/my-app-studio/issues/2).
- Stage-specific full check passed before commit/push: Black, Pylint, 98 foundation tests, 2 APP-001 contracts and 2 actual Chromium tests.
- Combined local app was previously checked through APP-003; that result does not substitute for this branch check.
- Predictions were not recorded before implementation; gaps remain explicit in LEARNING.md.
- GitHub PR, `check` and `windows` CI, merge and issue closure: Pending.
- Future lessons: APP-002 accounts and APP-003 roles remain outside this branch.
