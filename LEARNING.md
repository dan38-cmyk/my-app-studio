# Conversation evidence

Short AI-assisted summary, not a transcript or grade. Observations and decisions below are paraphrases of my replies, with grammar edits. Missing contributions remain Pending. The learner authorized publication after the final pre-push checks. Original missing predictions remain explicit.

**Writing assistance:** AI helped make my statements grammatically correct.

**Available conversation context:** Earlier November 1–6, 2026 work is available through the saved summaries below. The current chat includes local setup and Review 1 planning on November 15–16, 2026.

## Review 1 · Career research

- Selected sources: I supplied the Citi Python Developer, PGIM Data Analytics & Governance, and L3Harris Associate Software Engineering postings linked in SPEC. I said they match my résumé pretty well; specific matches still need to be assessed.
- Direction: I chose using data to improve business decisions. I approved AI's proposed early-career data analyst target and recruiters/hiring managers audience; the research compares this direction with software development.
- Plan approvals: I approved AI's evidence-first layout recommendation and the Home, Experience, Projects, Skills & Education, and Contact outline. The reason about helping recruiters find relevant evidence quickly was supplied by AI; no independent layout explanation or measured recruiter result is claimed.
- Approved experience summary: At Amazon, I tracked Delivery Estimated Accuracy (DEA) and served as my building’s DEA champion, helping improve the building’s accuracy. On the quality team, I also helped improve metrics including Perfect Scan Rate (PSR) and staging accuracy.
- Review: I approved the experience summary for accuracy in this chat before it was saved. No percentage improvement is attributed to these metrics.
- Help/gaps: AI organized the wording, compared the postings, mapped existing evidence and drafted the layout/page plan. I supplied the PGIM posting text after direct retrieval failed and reported the portfolio draft was accurate. Actual peer feedback/response remains pending. The RAG plan is now separately drafted below; no completed RAG app is claimed.

## Review 1 · RAG planning

- Topic decision: I accepted AI's suggestion to plan a data analyst learning assistant after choosing a data analytics career direction.
- Help/gaps: AI researched official sources and drafted the user/problem hypothesis, source permissions, vector/graph comparison, proposed import/retrieval/answer workflow, evaluation stories and resource constraints. I reviewed the draft and said it looked good; no independent learner explanation is claimed. Specific models and hosting capacity remain unresolved before Build.
- Review: Learner reported the draft looked good and subsequently authorized publication to the dan38-cmyk repository for peer review. This confirms approval of the record, not an executed technical evaluation.
- Checks / peer feedback: Not yet evidenced. Source reading occurred, but no RAG app tests or actual peer review have run.

## APP-001

- Prediction: Pending. No pre-implementation prediction was recorded.
- Check interpretation: The 390px browser check catches content extending beyond a narrow screen and requiring sideways scrolling. AI helped clarify that this specific check covers overflow, not every aspect of mobile usability.
- Browser observation: I like how the revised homepage presents my experience more effectively and helps me stand out immediately. My requested changes improved it by placing important facts up front, where they can catch a recruiter’s attention.
- Keep decision: Keep the revised homepage because the prominent facts help catch a recruiter’s attention.
- Review: Reviewed for accuracy before conditional publication approval.
- Help/gaps: I supplied IS117 Parts 1–3, my DegreeWorks audit and my résumé, and requested stronger recruiter-facing descriptions. AI helped implement the homepage, draft the copy and styling, add the course/work history, and run the checks. The original prediction remains missing; the completed App Studio homepage does not establish completion of the separate IS117 final.
- Evidence links / next step: [Issue #2](https://github.com/dan38-cmyk/my-app-studio/issues/2) closed; [PR #5](https://github.com/dan38-cmyk/my-app-studio/pull/5) merged with both CI jobs passing. Actual implementation/check links are in [SPEC.md](SPEC.md).

## APP-002

- Prediction: Pending. No before/after-login prediction was recorded.
- Check interpretation: The copied-cookie-after-logout check catches improper session invalidation, where an old login cookie could still grant account access after logout.
- Browser observation: I created an account, accessed the private dashboard, logged out and logged back in successfully.
- Keep decision: Keep the account features because they worked as expected in my tests.
- Review: Reviewed for accuracy before conditional publication approval.
- Help/gaps: AI connected the prepared security helpers to the browser forms and API routes and ran the full checks. My answer identifying improper session invalidation was edited for grammar. The original prediction remains missing.
- Evidence links / next step: [Issue #3](https://github.com/dan38-cmyk/my-app-studio/issues/3) closed; [PR #6](https://github.com/dan38-cmyk/my-app-studio/pull/6) merged with both CI jobs passing. Actual implementation/check links are in [SPEC.md](SPEC.md).

## APP-003

- Prediction: Pending. No pre-implementation direct-admin-request prediction was recorded.
- Check interpretation: AI-suggested explanation I approved: changing an admin back to a member while staying logged in removed access on the next request, showing that the server checks the current role rather than retaining the old admin permissions until logout.
- Browser observation: The admin page denied my member account, allowed access after I promoted it through the trusted local CLI, and denied access again after demotion while I stayed logged in.
- Direct API observation: I also requested `/api/admin` directly and reported denial as a member, access after promotion, and denial after demotion. Exact response bodies/status codes were not recorded from my browser; automated tests cover those separately.
- Keep decision: Keep the role features because the member/admin behavior worked as expected in my tests.
- Review: Reviewed for accuracy; publication authorized only after pre-push checks pass. Merge approval has not been given.
- Help/gaps: AI implemented and tested the server-side permission checks and supplied the local role-change commands and the suggested explanation above. My reported results are separate from the automated checks. The original prediction remains missing.
- Evidence links / next step: [Issue #4](https://github.com/dan38-cmyk/my-app-studio/issues/4), [PR #7](https://github.com/dan38-cmyk/my-app-studio/pull/7); implementation and actual check links in [SPEC.md](SPEC.md). Latest PR CI, owner-approved merge, issue closure and final main checks must be verified before completion.
