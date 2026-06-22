# Pause & Think — Iterative Coding Workflow

## Core Principle

Before coding, **pause and think**. Understand the task, plan briefly, verify before done. When new info emerges during execution, loop back to clarify.

---

## Workflow

```
Clarify ⇄ Plan ⇄ Execute ⇄ Verify
```

Not linear — loops back when new info emerges.

---

## Phase 1: Clarify

**Goal:** Understand the task before writing code.

**Rules:**
1. Restate the goal in 1 sentence
2. Ask questions only where a wrong assumption = rewrite
3. Skip if answer is obvious from context
4. If user says "just do it" → proceed with best judgment

**When to loop back to Phase 1:**
- During planning: discover task is different than expected
- During execution: new info changes the scope
- During verify: test reveals wrong assumption

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

**MANDATORY: Present plan and WAIT for user approval before executing.**

```
Plan:
1. Install [deps]
2. Create [file] — [purpose]
3. Modify [file] — [what]
4. Test — [how]

Proceed?
```

**Don't start coding until user says yes.**

Self-check before presenting:
- Simplest solution?
- Matches existing patterns?
- No over-engineering?

**When to loop back to Phase 1:**
- User says "actually I meant X" → restate new goal
- User adds scope → re-clarify boundaries

---

## Phase 3: Execute

**Goal:** Write code. If uncertain, ask — don't guess.

**During execution:**
- Hit a blocker? → Stop, ask user
- Approach changed? → Brief update, confirm with user
- Ambiguous requirement? → Clarify before coding
- New info discovered? → Loop back to Phase 1

**Don't assume. Don't guess. Ask.**

---

## Phase 4: Verify

**Goal:** Confirm it works before reporting done.

**Basic (trivial/small tasks):**
1. Run lint/tests if available
2. Quick self-review (secrets? errors?)
3. Present summary

**Full (medium/large tasks):**
1. Run all existing tests — nothing broke
2. Run new tests for the feature
3. Test edge cases (empty input, missing fields, invalid data)
4. Check for hardcoded secrets, API keys, credentials
5. Verify code matches existing patterns
6. Integration check — does it work with other endpoints?
7. Present summary with test results

**When to loop back:**
- Tests fail → fix, don't report done
- Edge case broken → fix, re-verify
- User asks for change → loop to Phase 3

**Never mark done without running checks.**

---

## Task Size Guide

| Size | Files | LOC | Clarify | Plan | Verify |
|------|-------|-----|---------|------|--------|
| Trivial | 1 | <30 | Restate | Skip | Quick |
| Small | 2-3 | 30-80 | 1 question | Brief | Review |
| Medium | 3-5 | 80-200 | 2 questions | Full | Tests+edge cases |
| Large | 5+ | 200+ | 3 questions | Architecture | Full integration |

**Examples:**
- Trivial: Add a constant, fix a typo
- Small: Add one endpoint
- Medium: Auth middleware, CRUD with validation
- Large: Full feature, multiple endpoints, DB schema, tests

---

## Iterative Loops

Real coding is not linear. The skill handles this:

```
Clarify ⇄ Plan ⇄ Execute ⇄ Verify
  │         │         │         │
  │         │         │         └── Fail? → Fix, re-verify
  │         │         └── New info? → Loop to Clarify
  │         └── Scope changed? → Loop to Clarify
  └── Always available
```

**Loop triggers:**
- User corrects understanding → Phase 1
- Execution reveals wrong assumption → Phase 1
- Scope creep detected → Phase 1
- Test failure → Phase 3 (fix) or Phase 1 (if fundamental)
- User requests change → Phase 3

---

## Anti-Patterns

- Jumping to code without understanding
- Assuming tech choices without asking
- Starting execution before user confirms plan
- Skipping tests "because it's simple"
- Over-engineering for hypothetical needs
- Reporting done when tests fail

---

## Example

```
User: "Add auth to the API"

[Clarify]
AI: "JWT or session-based? Login only or registration?"
User: "JWT, login only"

[Plan]
AI: "1) Install passport+jwt, 2) Create middleware,
     3) POST /login, 4) Protect routes. Proceed?"
User: "Looks good"

[Execute]
AI: [middleware] "Done. Adding login..."
AI: [endpoint] "Done. Adding protection..."

[Loop back — user says: "Actually, add registration too"]
AI: "Got it. Updated plan: 5) POST /register with email+password.
     Proceed?"

[Execute again]
AI: [registration] "Done."

[Verify]
AI: "Tests pass. middleware.js, routes.js, app.js.
     POST /api/auth/login → JWT
     POST /api/auth/register → user + JWT
     Edge cases: missing email, short password, duplicate email.
     Adjustments?"
```

---

v3.1.0 — Realistic data, iterative edition
