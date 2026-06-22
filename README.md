<div align="center">

# Pause & Think

### Iterative Coding Skill for AI Agents

> A structured workflow that forces AI to clarify, plan, and verify before reporting done.

</div>

---

## The Problem

AI coding agents typically:
- Jump straight into code without understanding the full task
- Make assumptions that turn out to be wrong
- Ship code without running tests
- User has to correct and redirect multiple times

This leads to wasted effort, frustration, and lower quality output.

## The Solution

**Pause & Think** enforces a simple 4-phase workflow:

```
Clarify → Plan → Execute → Verify
```

Instead of assuming and coding, the agent asks the right questions first, plans briefly, executes with checkpoints, and verifies before reporting done.

---

## How It Works

### Phase 1: Clarify

Before any code, ask 1-2 questions where a wrong assumption means rewriting later.

```
✅ Good: "JWT or session-based? Login only or registration?"
❌ Bad:  "What database? What framework? What language? What IDE?"
```

Skip if the answer is obvious from context. Don't over-question.

### Phase 2: Plan

Present a brief plan (max 10 lines) before writing code.

```
Plan:
1. Install passport + jsonwebtoken
2. Create auth/middleware.js — JWT verification
3. Create auth/routes.js — POST /login endpoint
4. Modify app.js — add auth routes, protect /api/*
5. Run existing tests to verify no breakage
```

### Phase 3: Execute

Write code. If you hit a blocker or ambiguity, stop and ask — don't guess.

### Phase 4: Verify

Before reporting "done":
- Run lint/tests if available
- Quick review for secrets, errors, patterns
- Present a summary of what was created/modified

---

## What It Prevents

| Anti-Pattern | How Skill Helps |
|-------------|----------------|
| Jumping to code without understanding | Phase 1 forces clarification |
| No planning | Phase 2 requires brief plan |
| Assuming tech choices | Phase 1 asks the right questions |
| Skipping tests | Phase 4 requires verification |
| Guessing when uncertain | Phase 3 says: stop and ask |
| Over-engineering | Phase 2 self-checks for simplicity |

---

## Task Size Guide

Not every task needs the full workflow:

| Size | Clarify | Plan | Verify |
|------|---------|------|--------|
| Trivial (1-2 steps) | Restate goal | Skip | Quick check |
| Small (3-5 steps) | 1 question | Brief plan | Self-review |
| Medium (5-15 steps) | 2 questions | Full plan | Run tests |
| Large (15+ steps) | 3 questions | Architecture | Full verification |

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
User: "Looks good"

[Execute]
AI: [writes middleware] "Done. Adding login endpoint..."
AI: [writes endpoint] "Done. Adding route protection..."

[Verify]
AI: "Tests pass. Created: middleware.js, routes.js.
     Modified: app.js. POST /api/auth/login → JWT.
     Any adjustments?"
```

---

## Quick Start

```bash
cp SKILL.md ~/.agents/skills/pause-and-think/SKILL.md
```

Then load the skill at the start of any coding task.

---

## Project Structure

```
pause-and-think/
├── SKILL.md      # Install this
├── README.md
└── charts/       # Visual references
    ├── chart-effectiveness.png
    ├── chart-efficiency.png
    ├── chart-scaling.png
    └── chart-tokens.png
```

---

## License

MIT

<div align="center">

**Built by [PaongLabs](https://github.com/farhanturu)**

</div>
