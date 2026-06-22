# Pause & Think — Iterative Coding Workflow

## Core Principle

Before coding, **pause and think**. Ask the minimum questions needed to get it right the first time.

> **1-2 good questions > 5 mediocre ones > 0 questions (assumptions)**

---

## Workflow

```
Clarify → Plan → Execute → Verify
```

---

## Phase 1: Clarify

**Goal:** Understand the task in ≤30 seconds.

**Rules:**
1. Restate the goal in 1 sentence
2. Ask **max 2 questions** — only where wrong = rewrite
3. Skip if answer is obvious from context
4. If user says "just do it" → skip to Phase 2

**What to ask (pick relevant only):**
- Tech stack? (DB, framework) — ask if ambiguous
- Scope? (what's in/out) — ask if scope unclear
- New or existing code? — ask if context missing

**What NOT to ask:**
- Style preferences (tabs/spaces, colors)
- Obvious choices (use existing DB, not switch)
- Hypotheticals ("what if you need X later?")

**Example:**
```
✅ "JWT or session-based? Login only or registration?"
❌ "What database? What framework? What language? What IDE? What color scheme?"
```

---

## Phase 2: Plan

**Goal:** Confirm approach. Max 10 lines.

```
Plan:
1. Install [deps]
2. Create [file] — [purpose]
3. Modify [file] — [what]
4. Test — [how]
```

**Self-check:** Simplest solution? Matches existing patterns? No over-engineering?

**Rule:** >10 lines → split into sub-tasks.

---

## Phase 3: Execute

**Goal:** Code in focused bursts.

**Checkpoints:**
- Every ~80 lines: "On plan? Clean? Duplication?"
- 50% done: brief update to user
- Blocker → STOP, ask user

**Rule:** Never write 200+ lines without checking in.

---

## Phase 4: Verify

**Goal:** Confirm it works.

1. Run lint/tests
2. Self-review (secrets? errors? patterns?)
3. Summary:
   ```
   Done. Created: [files]. Modified: [files].
   [Key feature]. Adjustments?
   ```

**Rule:** Never mark done without running checks.

---

## Task Size Guide

| Size | Clarify | Plan | Execute | Verify |
|------|---------|------|---------|--------|
| Trivial | Restate | Skip | Run | Quick |
| Small | 1 question | Brief | +check | Review |
| Medium | 2 questions | Full | +checkpoints | Test |
| Large | 3 questions | Arch | Phased | Full |

---

## Smart Checks

- **Scope:** "Is this 2 tasks?" → Split, confirm priority.
- **Deps:** New package? → Confirm first.
- **Failure:** "What could go wrong?" → Handle it.
- **Reversible:** "Can this be undone?" → Plan rollback.

---

## Anti-Patterns

- ❌ 5+ questions for a simple task
- ❌ 300+ lines without a checkpoint
- ❌ Assuming tech choices
- ❌ Skipping tests
- ❌ Over-engineering

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

v1.2.0 — Optimized edition
