# App Studio decisions

## Review 1 · Individual planning record

This section extends the existing record for the November 17, 2026 Plan review. It does not declare completion of the review or change application behavior.

### 1. Portfolio + career research

- Learner-selected direction: use data to improve business decisions. Comparison: data analytics/governance versus software development. Learner approved the AI-proposed target of early-career data analyst and audience of recruiters and hiring managers.
- Original employer sources selected by the learner:
  - [Citi — Python Developer, Officer](https://jobs.citi.com/job/new-york/python-developer-officer/287/103168822352): AI read the employer page during this chat; responsibilities include Python pipelines, SQL, data quality, testing and documentation.
  - [PGIM — Analyst/Associate, Data Analytics & Governance](https://pru.wd5.myworkdayjobs.com/en-US/careers/job/Newark-NJ-USA/PGIM-Real-Estate---Analyst-Associate--Data-Analytics---Governance_R-125266-2): Learner supplied the posting text (requisition R-125266) after direct retrieval failed. It describes data quality monitoring, source lineage, requirements, reporting and validation. Requirements include a relevant bachelor's degree, 1–3 years of relevant experience, SQL, advanced Excel and BI experience. The pasted text is the basis for this summary; live availability was not independently confirmed.
  - [L3Harris — Associate, Software Engineering](https://careers.l3harris.com/en/job/clifton/associate-software-engineering/4832/100443672240): AI read the employer page during this chat; responsibilities include embedded software development, testing, documentation and peer review.
- Learner-approved work evidence: tracked Delivery Estimated Accuracy (DEA), served as the building’s DEA champion and helped improve building accuracy; quality-team work included Perfect Scan Rate (PSR) and staging accuracy. No new quantified result is claimed. Existing résumé percentages are not attributed to these metrics.
#### Career alternatives · AI-drafted analysis

| Direction | Employer evidence | Relevant existing evidence | Limits / development needs |
|---|---|---|---|
| Data analytics / governance | PGIM emphasizes reliable datasets, quality metrics, reports, validation and business collaboration. Citi also includes pipeline data quality and governance, showing overlap between analytics and development. | Learner-confirmed DEA, PSR and staging-accuracy work; saved résumé-derived portfolio includes an Excel defect dashboard and operational-data coaching. | Operational metrics experience does not establish formal governance, financial-services knowledge or proficiency in SQL, Power BI, semantic models or lineage tools. Degree is in progress. |
| Software development | Citi emphasizes Python/SQL pipelines, reusable services, testing and deployment; L3Harris emphasizes embedded software, integration, test procedures and defect review. | Existing AI-assisted FastAPI portfolio/accounts/roles project and recorded Python, database and internet-applications coursework. | Coursework and an AI-assisted app do not establish independent proficiency, production pipeline experience, embedded/real-time experience or expertise in every listed language. |

The learner chose using data to improve business decisions and approved AI's proposed focus on early-career data analyst roles and recruiters/hiring managers. The Amazon quality work provides concrete operational context, while PGIM exposes technical skills that need evidence or development.

#### Responsibility-to-evidence map · proposed portfolio emphasis

| Employer responsibility | Available evidence | Boundary |
|---|---|---|
| PGIM: monitor data quality and report metrics | Learner-confirmed DEA champion and quality-team work on PSR/staging accuracy | No newly claimed percentage, formal data governance program or specific BI tool. |
| PGIM: prepare reports and investigate unexpected results | Saved résumé-derived `app/portfolio.json` describes Excel defect tracking and delivery-discrepancy investigation | Historical résumé summary, not independently audited employer results; no confidential Amazon data should be published. |
| PGIM: work with business/technical colleagues | Saved résumé-derived portfolio describes cross-shift standard work and cross-department coordination | Does not establish investment-domain experience. |
| Citi/L3Harris: test software and document work | Existing app source, contracts and Studio evidence in this record | AI-assisted work; latest local full check failed one Windows symbolic-link permission test, despite passing 18 lesson contracts and 2 Chromium journeys. |

#### Page outline and layout decision

The learner approved this AI-proposed outline. It is planned information architecture; the existing app uses homepage sections, and these approvals do not establish that separate pages have been built.

| Planned page | Purpose and content |
|---|---|
| Home | State the data analyst direction and feature DEA/quality-metrics experience with links to supporting work. |
| Experience | Explain Amazon DEA, PSR and staging-accuracy contributions; retain other résumé-supported work and distinguish responsibilities from outcomes. |
| Projects | Show actual projects, repository/check links, individual contribution and AI assistance. RAG remains planned until work exists. |
| Skills & Education | Link demonstrated skills to work/course evidence, distinguish learning goals from proficiency, and label the bachelor's degree in progress. |
| Contact | Provide the existing public GitHub contact route; additional contact details need explicit approval. |

| Lightweight layout | Benefit | Tradeoff |
|---|---|---|
| Evidence first: role statement, featured operational evidence/projects, then skills and education | Makes job-relevant examples easy for recruiters to find. This is the AI-proposed rationale, not an observed recruiter result. | Short summaries need links/context so metrics are not presented without explanation. |
| Biography first: background introduction, then experience and projects | Gives personal/career-transition context before examples. | Relevant evidence appears later and may take longer to locate. This is a design assumption, not a measured result. |

Decision: learner approved the AI-recommended evidence-first layout. Approval records adoption; no separate learner-authored layout rationale or user test is claimed.

- Peer review: Pending. Ask a peer to inspect the employer sources and evidence map: does the target reader and featured experience follow from those sources, and is any claim unsupported? Record their actual feedback, the learner's response and any resulting revision here.
- Review: learner reported the portfolio research draft was accurate ("all good") and authorized publication for peer review. Actual peer feedback/response remains pending.
- Changed: selected three sources; recorded career comparison, approved target/audience and experience example; added the approved page outline and layout choice.
- Checked: AI retrieved Citi and L3Harris employer text and read the learner-supplied PGIM text. Compared responsibilities against the approved experience summary and saved résumé-derived portfolio. These are document comparisons, not application tests or proof of job eligibility.
- Next: obtain real peer feedback and record the response before finalizing the portfolio section.

### 2. RAG app + technical research

#### Scope and research question

The learner approved the AI-proposed **data analyst learning assistant** topic. The following technical plan is AI-drafted for review, not a built application or independently explained learner architecture.

- Reader: a beginner studying SQL and pandas for data analyst work.
- Problem hypothesis: beginners need help locating relevant official explanations and distinguishing SQL operations from pandas operations. No user research has yet established frequency or demand.
- Research question: can a small, versioned collection of official tutorials support useful beginner answers with inspectable supporting passages and honest handling of missing evidence?
- Proposed scope: explain selecting/filtering, aggregation and combining tables, with source links. No employer data, arbitrary uploads, execution of user code, career promises or unrestricted web search.

#### Research-review index and original sources

Sources were opened by AI during this planning chat. Source facts below are distinct from design proposals. Learner verification and peer review remain pending.

| Source | Finding / use |
|---|---|
| [PostgreSQL tutorial](https://www.postgresql.org/docs/18/tutorial.html) | Beginner SQL source collection; pin the major version rather than silently follow a changing current alias. |
| [PostgreSQL license](https://www.postgresql.org/about/licence/) | Explicitly permits reuse of software and documentation subject to retaining its notices. Preserve notices with imported copies. |
| [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) | Candidate material for table selection, summary statistics and combining tables. Record the actual version and retrieval date when importing. |
| [pandas project license](https://github.com/pandas-dev/pandas/blob/main/LICENSE) | BSD 3-Clause terms; retain applicable notices and disclaimers. Confirm selected documentation files and bundled examples have no additional notices before import; exclude separately licensed linked datasets/images. |
| [RAG research paper, Lewis et al.](https://arxiv.org/abs/2005.11401) | Describes combining a retriever and a generator. Retrieval supplies evidence; it does not guarantee correct generated claims. |
| [Sentence Transformers semantic search](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) | Documents embedding queries/passages into a common vector space and ranking similar passages. Model suitability for short questions versus longer passages matters. |
| [pgvector](https://github.com/pgvector/pgvector) | Documents vector similarity search in PostgreSQL. Candidate vector storage without a separate vector database service. |
| [Neo4j graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/) | Nodes and relationships provide an explicit graph representation; useful for comparing a concept/dependency graph alternative. |
| [PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch.html) | Keyword retrieval baseline to compare with semantic retrieval before claiming improvement. |

#### Compare before choosing

| Approach | Proposed representation / retrieval | Benefit for this problem | Cost / limitation |
|---|---|---|---|
| Vector RAG | Embed documentation passages and questions; rank by similarity and filter by tool/version. | May retrieve explanations when a beginner uses different words from the documentation. | Similarity can return the wrong operation or tool; requires model choice, evaluation and source inspection. |
| Graph RAG | Nodes for tools, operations, pages and versions; edges such as DOCUMENTS, BELONGS_TO and REQUIRES; retrieve via explicit relationships. | Makes dependencies and multi-step concept relationships inspectable. | Requires a verified schema, entity extraction and relationship maintenance; a graph alone does not solve paraphrase matching. |

AI-recommended initial decision: **vector RAG**, with PostgreSQL/pgvector proposed for metadata and vectors and a keyword baseline for evaluation. The initial questions concern explanations in passages, rather than multi-hop relationships. Do not add a separate graph service until an evaluation need justifies it. Graph databases can also support vector indexes; this comparison is about proposed representations, not mutually exclusive product capabilities. Learner reviewed the draft and said it looked good; no independent explanation of this recommendation is claimed.

#### Proposed import, representation and architecture

1. Maintain a small allowlist (initial cap: 20 tutorial pages). Check licenses/notices, URLs and versions; fetch at a low rate and cache permitted copies. Exclude private, login-only and unrelated linked content.
2. Extract main text, headings and code examples, removing menus. Split at headings into passages with a provisional 300–600-token target and limited overlap. Keep code/explanations together when practical. Chunking trades retrieval focus against missing context; inspect examples and adjust rather than treating these numbers as proven.
3. Store source URL, title, heading anchor, version, fetch date, license reference, content hash and stable chunk ID. Upsert by source/version/hash so repeat import does not duplicate content. Report empty/failed imports instead of silently indexing them.
4. Embed chunks using one pinned, license-checked sentence embedding model. An embedding is a numeric representation used for similarity, not a guarantee of truth. Store the model identifier/dimension with vectors; re-embed when the model changes.
5. A proposed separate FastAPI RAG application accepts a bounded question and SQL/pandas selection, embeds the query using the same model and retrieves up to four matching passages. No changes to the working portfolio or its account database are authorized by this plan.
6. Supply only retrieved evidence to a selected text-generation model, requesting a concise answer with chunk-linked citations. Evidence is data, not instructions. If retrieval is inadequate, report insufficient evidence. Similarity alone cannot prove support; validate answer support in evaluation. Show cited passages so a reader can inspect them.
7. Generation/embedding model identifiers, licenses, memory use and hosting route are decision gates before Build. No API key, purchase, provider account, dependency installation or deployment is needed for Plan. An excerpt-only search prototype may validate retrieval, but must be labeled as such and is not a finished generative RAG app.

#### One proposed source-to-answer trace

Source: [PostgreSQL 18 aggregate tutorial](https://www.postgresql.org/docs/18/tutorial-agg.html). It explains grouping and the distinction between WHERE and HAVING. Import its main text and examples; attach its URL/heading/version to a chunk; embed and store that chunk. For “How do I filter groups after calculating totals?”, retrieve the aggregate passage. The proposed answer explains HAVING with a link to that exact evidence. A reviewer checks whether the passage actually supports the answer and whether the system accidentally recommends WHERE for the aggregate condition. This is a manually designed trace, **not an executed retrieval or generation result**.

#### Evaluation questions and five observable stories · all planned

| Story / input | Expected observable behavior | Defect it could expose |
|---|---|---|
| 1. Beginner asks “How do I filter groups after calculating totals?” with SQL selected | Aggregate/HAVING evidence appears in top four; answer distinguishes row filtering from group filtering and cites the source. | Missed paraphrase, unsupported answer or WHERE/HAVING confusion. |
| 2. Beginner asks “How do I calculate the average for each category?” with pandas selected | Retrieve supporting [pandas summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html) passages; explain groupby/mean with a supporting citation rather than SQL syntax. | Wrong-tool retrieval or code with no source support. |
| 3. Reader asks “What was Amazon's internal DEA target last week?” | State the approved collection does not contain that information; invent no target or citation. | Hallucinated private or out-of-scope facts. |
| 4. Maintainer imports an unchanged allowlisted source twice | Same chunk count/identifiers; source/version/license metadata remains intact; failures are visible. | Duplicate or untraceable imported evidence. |
| 5. Reader opens an answer and its citation on desktop/narrow view | Question, answer and cited passages remain usable; citation resolves to the recorded source section; model timeout produces a clear retry/error state. | Broken evidence links, unusable layout or hidden failures. |

Proposed evaluation: keep a versioned question set with expected supporting sections and assess retrieval separately from generation. Record retrieved IDs/ranks, answer claims/citations and actual latency for each run. Compare keyword and vector results on the same questions; inspect every initial answer for evidence support. Initial acceptance: both in-scope questions retrieve the correct supporting passage in the top four, every substantive answer claim has supporting evidence, the unsupported question abstains, and import/citation/UI stories pass. This small suite cannot establish general accuracy. No success rate, speed advantage or passed test is claimed.

#### Hosting and resources · unverified planning constraints

- Local development first; no hosted RAG URL exists. Hosting will be a separate agreed step through Server Studio, without changing this repository's deployment/proxy configuration.
- Start with at most 20 pages, capped imports/question/context sizes and cached offline embeddings. Avoid GPU assumptions and unbounded crawls.
- Before choosing models, inspect available RAM/CPU/disk, PostgreSQL/pgvector support, model-download sizes, CPU latency and license terms. A local generator may exceed the host's resources; hosted inference has privacy, network and cost constraints requiring a separate decision. No costs or capacity are verified.
- Proposed initial generation timeout: 30 seconds with a visible failure state; this is an engineering limit to evaluate, not measured performance.

- Peer review: Pending. Ask a peer to follow the aggregate-source trace, identify one unsupported assumption/tradeoff and explain how an evaluation question would reveal missing/incorrect evidence. Record actual feedback, decision and changed documentation here.
- Changed: learner selected the data analyst learning assistant topic; AI drafted source research, alternatives, proposed architecture, trace and evaluation stories.
- Checked: AI opened the linked original documentation, licenses and research. The aggregate and pandas pages contain relevant example material. No corpus was imported, models installed, retrieval executed, answer generated by the proposed app or hosting tested. A documentation trace is not a test run.
- Review: learner reported the draft looked good and authorized publication for peer review. Source reading by AI is distinguished from independent learner verification and executed tests.
- Next: obtain actual peer feedback and record the response; resolve model/hosting gates before implementation. Publication of this plan does not establish a hosted RAG app.

Group planning is a separate submission. The learner reports no partner yet; no shared decisions, partner contributions or peer feedback are claimed here.

## Current state

- **Scope:** Local Daniel Nizami portfolio based on the learner's IS117 planning, plus APP-002 accounts and APP-003 roles as explicitly requested in this chat on November 6, 2026.
- **Implementation:** APP-001–003 implemented and separated into cumulative lesson branches: `app-001-homepage`, `app-002-accounts`, `app-003-roles`. Full branch checks are required before each commit/push. Homepage PR #5 and accounts PR #6 are merged, and both required jobs passed on each PR. [Roles PR #7](https://github.com/dan38-cmyk/my-app-studio/pull/7) is open; its latest CI, merge, issue closure and final main checks must be verified.
- **Next step:** Verify both jobs on the latest roles PR commit before owner-approved merge, then verify issue #4 closure and the final main checks. Original missing predictions remain explicit.
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
| Issue / branch / PR | [APP-001 issue #2](https://github.com/dan38-cmyk/my-app-studio/issues/2) is closed after [PR #5](https://github.com/dan38-cmyk/my-app-studio/pull/5) merged; both PR CI jobs passed. Local branch `app-001-homepage`; three lesson publication cycles remain required. |

## APP-002 · Accounts

**Authorized scope:** Signup, login, private dashboard and logout, through browser forms and JSON APIs. The public portfolio remains accessible without login. Accounts use the prepared SQLite, Argon2id password hashing, signed expiring JWT cookie, CSRF and server-side revocation helpers. JWT signatures do not encrypt their contents. Cookies are HttpOnly, SameSite and configured Secure in production; local development remains loopback-only.

- Browser pages/forms: `/signup`, `/login`, `/dashboard`, POST `/logout`.
- API: GET `/api/csrf`, POST `/api/signup`, POST `/api/login`, GET `/api/me`, POST `/api/logout`.
- New accounts are members; role fields are rejected. Wrong credentials use a generic error. Normalized usernames are retained after recoverable form errors; passwords are never reflected or returned.
- Prepared rate limits apply to signup/login. Logout revokes the server session, so replaying a copied cookie fails.
- Implementation: `app/features/accounts.py`, `app/templates/account.html`, `app/templates/dashboard.html`.
- [APP-002 issue #3](https://github.com/dan38-cmyk/my-app-studio/issues/3) is closed after [PR #6](https://github.com/dan38-cmyk/my-app-studio/pull/6) merged; both PR CI jobs passed. Learner reports successful signup, dashboard access, logout and repeat login; they identified improper session invalidation as the bug caught by the copied-cookie/logout test and chose to retain the tested features because they worked as expected. No production deployment, recovery or email-verification feature is claimed.

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
- [APP-003 issue #4](https://github.com/dan38-cmyk/my-app-studio/issues/4) verified open with the correct lesson marker; [PR #7](https://github.com/dan38-cmyk/my-app-studio/pull/7) is open. Learner confirmed browser member denial, admin access after trusted CLI promotion, and renewed denial after demotion while remaining logged in. Direct API behavior is covered by automated tests; learner also reported direct API denial, access after promotion, and denial after demotion. The role-test explanation was approved with AI assistance; learner chose to keep the working role features.

**Publication sequence:** The learner requested the local features together. Publication is split into three dependent lesson PRs: homepage → accounts → roles. Actual verified URLs and run results are recorded below; no retrospective claim of earlier PRs is made.

## Actual checks

Full local checks were run progressively on November 6, 2026 without changing prepared assertions or security helpers:

| Scope | Results |
|---|---|
| APP-001 | Black/Pylint passed; 98 foundation tests, 2 homepage contracts and 2 Chromium tests passed on the isolated homepage-only publication branch. |
| APP-002 | Black/Pylint passed; 98 foundation tests, 14 cumulative contracts and 2 Chromium tests passed on the isolated accounts publication branch. |
| APP-003 | Black/Pylint passed; 98 foundation tests, 18 cumulative contracts and 2 Chromium tests passed. The role browser journey used isolated disposable data and exercised member denial, trusted CLI promotion, admin access, demotion and revoked-cookie replay. |
| Final normal check after marker update | Passed on the combined local app after the recruiter-copy revision: Black, Pylint, 98 foundation tests, 18 cumulative lesson contracts and 2 real Chromium tests. |
| GitHub CI (`check` and `windows`) | Both jobs passed for homepage PR #5 and accounts PR #6. [Roles PR #7 latest checks](https://github.com/dan38-cmyk/my-app-studio/pull/7/checks) and final main results must be verified before completion. |

AI inspected the rendered desktop homepage through Chrome and reviewed full-page 390px screenshots of the current homepage and signup form from the isolated Chromium fixture. No clipping or horizontal overflow was observed in those captures; the focused keyboard/mobile test also passed. The saved full APP-003 check receipt matches the current application source. The final diff has no whitespace errors, and the reviewed public files exclude the original private documents, local databases, signing keys and personal contact details. Tests emit a pre-existing FastAPI/Starlette TestClient deprecation warning; the checks pass without changing pinned dependencies.

Local preview: `http://127.0.0.1:8000`. This is not a submission or production URL. Final submission will be the completed accessible repository at `https://github.com/dan38-cmyk/my-app-studio`, after the required reviewed issues/PRs, both CI jobs and main-branch checks. Local passes do not establish GitHub completion or learner understanding.

**Final isolated APP-003 publication branch check:** Passed before commit/push: Black, Pylint, 98 foundation tests, 18 cumulative lesson contracts and 2 actual Chromium tests.

## Verified GitHub evidence

| Lesson | Issue / PR | Actual passing PR CI | Merge and main evidence |
|---|---|---|---|
| APP-001 | [Issue #2](https://github.com/dan38-cmyk/my-app-studio/issues/2), [PR #5](https://github.com/dan38-cmyk/my-app-studio/pull/5) | [check](https://github.com/dan38-cmyk/my-app-studio/actions/runs/42325363444/job/128259261842), [windows](https://github.com/dan38-cmyk/my-app-studio/actions/runs/42325363444/job/128259262030) | PR merged, issue closed; [main run](https://github.com/dan38-cmyk/my-app-studio/actions/runs/42325746946) passed both jobs. |
| APP-002 | [Issue #3](https://github.com/dan38-cmyk/my-app-studio/issues/3), [PR #6](https://github.com/dan38-cmyk/my-app-studio/pull/6) | [check](https://github.com/dan38-cmyk/my-app-studio/actions/runs/42325867355/job/128260893554), [windows](https://github.com/dan38-cmyk/my-app-studio/actions/runs/42325867355/job/128260893143) | PR merged, issue closed; [main run](https://github.com/dan38-cmyk/my-app-studio/actions/runs/42326135929) passed both jobs. |
| APP-003 | [Issue #4](https://github.com/dan38-cmyk/my-app-studio/issues/4), [PR #7](https://github.com/dan38-cmyk/my-app-studio/pull/7) | Local full checks passed; inspect [latest PR check and windows results](https://github.com/dan38-cmyk/my-app-studio/pull/7/checks). | Verify PR merge, issue closure and final main checks after approval. |
