# Pause & Think — Iterative Coding Workflow

## Core Principle

Before coding, **pause and think**. Ask the minimum questions needed to get it right the first time. This saves more tokens than it costs.

## Workflow: 4 Phases

```
Clarify → Plan → Execute → Verify
  🔵       🟡      🟢       ✅
```

---

## Phase 1: Clarify (1-2 Questions MAX)

**Goal:** Understand the task in ≤60 seconds.

**How:**
1. Restate the goal in 1 sentence
2. Ask only questions where a wrong assumption = rewrite:
   - Tech stack choice (DB, framework, language)
   - Scope boundary (what's included, what's not)
   - Existing code or new project
3. Skip questions where the answer is obvious from context

**Example — Good (2 questions):**
> "Got it — add auth to Express. Quick questions:
> 1. JWT or session-based?
> 2. Login only, or also registration?"

**Example — Bad (5 questions, overkill):**
> "Before I start: 1. What's your favorite color? 2. Do you prefer tabs or spaces? ..."

**Rule:** If user says "just do it" → skip to Phase 2, restate goal only.

---

## Phase 2: Plan (10 Lines Max)

**Goal:** Confirm approach before writing code.

**Output:**
```
Plan:
1. Install [deps]
2. Create [file] — [purpose]
3. Modify [file] — [what changes]
4. Test — [how]
```

**Self-check before presenting:**
- Is this the simplest solution? (YAGNI)
- Does it match existing code patterns?
- Am I over-engineering?

**Rule:** If plan is >10 lines, split into sub-tasks.

---

## Phase 3: Execute (Checkpoint Every ~80 Lines)

**Goal:** Write code in focused bursts.

**Checkpoints:**
- Every ~80 lines: "Still on plan? Code clean? Any duplication?"
- At 50%: brief progress update to user
- Blocker hit → STOP, ask user (don't guess)

**Rule:** Never write 200+ lines without a micro-check.

---

## Phase 4: Verify

**Goal:** Confirm everything works before reporting done.

**Steps:**
1. Run lint/format/tests
2. Quick self-review (secrets? errors? patterns?)
3. Present summary:
   ```
   Done. Created: [files]. Modified: [files].
   Endpoint: POST /api/...
   Any adjustments?
   ```

**Rule:** Never mark done without running checks.

---

## Task Size Guide

| Size | Clarify | Plan | Execute | Verify |
|------|---------|------|---------|--------|
| Trivial (1-2 steps) | Restate only | Skip | Run | Quick check |
| Small (3-5) | 1 question | Brief plan | +micro-check | Self-review |
| Medium (5-15) | 2 questions | Full plan | +checkpoints | Review+test |
| Large (15+) | 3 questions | Architecture | Phased exec | Full verify |

---

## Smart Thinking Patterns

**Scope check:** "Is this actually 2 tasks?" → Split, confirm priority.

**Dependency check:** New package needed? → Confirm with user first.

**Failure check:** "What could go wrong?" → Handle edge cases.

**Reversibility:** "Can this be undone?" → Plan rollback if not.

---

## Anti-Patterns

- ❌ 5+ clarifying questions for a simple task
- ❌ Writing 300+ lines without a checkpoint
- ❌ Assuming tech choices without asking
- ❌ Skipping tests "because it's simple"
- ❌ Over-engineering for hypothetical needs

---

## Example

```
User: "Add auth to the API"

[Clarify — 2 questions]
AI: "JWT or session-based? Login only or also registration?"
User: "JWT, login only"

[Plan — 5 lines]
AI: "Plan: 1) Install passport+jwt, 2) Create middleware,
     3) POST /login endpoint, 4) Protect /api/* routes. Go?"

[Execute — with checkpoints]
AI: [writes middleware] "Middleware done. Adding login endpoint..."
AI: [writes endpoint] "Endpoint done. Adding route protection..."

[Verify]
AI: "All tests pass. Created: auth/middleware.js, auth/routes.js.
     Modified: app.js. POST /api/auth/login — returns JWT. Adjustments?"
```

---

v1.1.0 — Concise edition
