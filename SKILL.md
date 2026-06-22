# Pause & Think — Iterative Coding Workflow

## Core Principle

Before coding, **pause and think**. Understand the task, plan briefly, verify before done.

---

## Workflow

```
Clarify → Plan → Execute → Verify
```

---

## Phase 1: Clarify

**Goal:** Understand the task before writing code.

**Rules:**
1. Restate the goal in 1 sentence
2. Ask questions only where a wrong assumption = rewrite
3. Skip if answer is obvious from context
4. If user says "just do it" → proceed with best judgment

**What to ask (only when ambiguous):**
- Tech stack? (DB, framework)
- Scope? (what's in/out)
- New or existing code?

**Don't ask:**
- Style preferences (tabs/spaces)
- Obvious choices (use existing DB)
- Hypotheticals ("what if X later?")

---

## Phase 2: Plan

**Goal:** Confirm approach before writing code.

Present a brief plan:
```
1. Install [deps]
2. Create [file] — [purpose]
3. Modify [file] — [what]
4. Test — [how]
```

Self-check: Simplest solution? Matches patterns? No over-engineering?

---

## Phase 3: Execute

**Goal:** Write code. If uncertain, ask — don't guess.

- Hit a blocker? → Stop, ask user
- Approach changed? → Brief update to user
- Ambiguous requirement? → Clarify before coding

---

## Phase 4: Verify

**Goal:** Confirm it works before reporting done.

1. Run lint/tests if available
2. Quick self-review (secrets? errors?)
3. Present summary:
   ```
   Done. Created: [files]. Modified: [files].
   [Key feature]. Any adjustments?
   ```

Never mark done without running checks.

---

## Task Size Guide

| Size | Clarify | Plan | Verify |
|------|---------|------|--------|
| Trivial | Restate | Skip | Quick |
| Small | 1 question | Brief | Review |
| Medium | 2 questions | Full | Test |
| Large | 3 questions | Arch | Full |

---

## Anti-Patterns

- Jumping to code without understanding
- Assuming tech choices without asking
- Skipping tests "because it's simple"
- Over-engineering for hypothetical needs

---

## Example

```
User: "Add auth to the API"

[Clarify]
AI: "JWT or session-based? Login only or registration?"
User: "JWT, login only"

[Plan]
AI: "1) Install passport+jwt, 2) Create middleware,
     3) POST /login, 4) Protect routes. Go?"

[Execute]
AI: [middleware] "Done. Adding login..."
AI: [endpoint] "Done. Adding protection..."

[Verify]
AI: "Tests pass. middleware.js, routes.js, app.js.
     POST /api/auth/login → JWT. Adjustments?"
```

---

v2.1.0 — Evidence-based edition
