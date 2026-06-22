# Pause & Think — Iterative Coding Workflow

## Overview

This skill forces AI coding agents to **pause, reflect, and clarify** at structured checkpoints instead of coding continuously. It produces higher-quality code by interleaving thinking phases with execution phases.

## Core Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  PHASE 1    │────▶│  PHASE 2    │────▶│  PHASE 3    │────▶│  PHASE 4    │
│  Clarify    │     │  Plan       │     │  Execute    │     │  Verify     │
│  & Understand│    │  & Design   │     │  & Code     │     │  & Refine   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
       ▼                   ▼                   ▼                   ▼
   [Ask User]        [Self-Check]       [Checkpoint]        [User Review]
```

## Phase Definitions

### PHASE 1: Clarify & Understand (MANDATORY FIRST)

**Purpose**: Ensure you fully understand the task before writing any code.

**Checkpoint 1 — Restate the Goal:**
- Paraphrase the user's request in your own words
- List what you understand: goal, constraints, tech stack, edge cases
- List what you DON'T understand or need to confirm

**Checkpoint 2 — Ask Clarifying Questions:**
- Use the `question` tool to ask 2-5 specific questions about:
  - Scope: "Should this handle X as well, or just Y?"
  - Style: "Do you prefer option A or B?"
  - Priority: "What's most important — speed, readability, or flexibility?"
  - Context: "Is this a new project or modifying existing code?"
- Wait for answers before proceeding

**Checkpoint 3 — Confirm Understanding:**
- Summarize: "Here's what I'll do: [list]. Is this correct?"
- Get explicit user confirmation: "Yes, proceed" or corrections

**Rules:**
- NEVER skip Phase 1 for non-trivial tasks (3+ steps)
- If the user says "just do it", still do a mini version (restate goal, proceed)
- If clarification reveals the task is different, STOP and re-assess

### PHASE 2: Plan & Design

**Purpose**: Think through the solution before writing code.

**Checkpoint 4 — Architecture Decision:**
- State your approach in 2-3 sentences
- List files you'll create/modify
- Note any dependencies or libraries you'll use
- Flag any risks or tradeoffs

**Checkpoint 5 — Self-Check:**
- "Does this approach align with the project's existing patterns?"
- "Am I over-engineering this?" (apply YAGNI)
- "What's the simplest solution that works?"

**Checkpoint 6 — Present Plan to User:**
- Show a brief plan: "I'll: 1) create X, 2) modify Y, 3) test Z"
- Wait for approval or feedback
- Adjust if user suggests alternatives

**Rules:**
- Keep the plan concise (5-10 lines max)
- If the plan is complex, break it into sub-tasks
- Revisit Phase 2 if Phase 3 reveals unexpected complexity

### PHASE 3: Execute & Code

**Purpose**: Write code in focused bursts with internal checkpoints.

**Checkpoint 7 — Start Coding:**
- Begin with the most foundational piece first
- Write in logical order (types → utils → components → tests)

**Checkpoint 8 — Micro-Checkpoint (every 50-100 lines):**
- Pause and ask yourself:
  - "Am I still following the plan from Phase 2?"
  - "Is this code clean and readable?"
  - "Have I introduced any duplication?"
- If something is off, correct it before continuing

**Checkpoint 9 — Midpoint Review:**
- At ~50% completion, summarize progress:
  - "Done: [list]. Remaining: [list]."
  - "I noticed [issue] during coding, adjusting approach."
- If the plan needs changing, go back to Phase 2 briefly

**Rules:**
- Never write more than 100 lines without a micro-checkpoint
- If you hit a blocker, STOP and ask the user (don't guess)
- Prefer incremental commits/changes over one big batch

### PHASE 4: Verify & Refine

**Purpose**: Validate the solution and ensure quality.

**Checkpoint 10 — Self-Review:**
- Read through all changes you made
- Check for:
  - Consistency with existing code patterns
  - Error handling at boundaries
  - No hardcoded secrets or sensitive data
  - Comments only where genuinely needed
- Run lint/format commands if available

**Checkpoint 11 — Test:**
- Run existing tests to ensure nothing broke
- Write tests for new functionality (if applicable)
- Manual verification if no test suite exists

**Checkpoint 12 — Final Summary:**
- Present to user: "Here's what I did: [summary]"
- List files changed: "Modified: X, Y. Created: Z."
- Note any follow-up items or known limitations
- Ask: "Does this look good, or should I adjust anything?"

**Rules:**
- Never mark task as done without running checks
- If tests fail, fix them before reporting success
- If user asks for changes, loop back to Phase 3

## Decision Matrix

Use this to determine how thorough each phase should be:

| Task Size | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|-----------|---------|---------|---------|---------|
| Trivial (1-2 steps) | Skip questions, restate only | Skip | Execute | Quick check |
| Small (3-5 steps) | Mini clarify (1-2 questions) | Brief plan | Execute + micro-check | Self-review |
| Medium (5-15 steps) | Full clarify (2-3 questions) | Detailed plan | Execute + checkpoints | Review + test |
| Large (15+ steps) | Deep clarify (3-5 questions) | Architecture plan | Phased execution | Full verification |

## Clarification Sections (Agent Intelligence Boosters)

These sections train the AI to think smarter about common patterns:

### A. Scope Creep Detection
Before starting, ask: "Is this task actually multiple tasks?" If yes:
- Split into sub-tasks
- Confirm priority order with user
- Tackle one at a time

### B. Dependency Check
Before coding, check:
- Does this require a new package? → Confirm with user
- Does this conflict with existing code? → Investigate first
- Does this need database/API changes? → Plan accordingly

### C. Failure Mode Thinking
Before finishing, ask: "What could go wrong?"
- Network failures → add retry/error handling
- Invalid input → add validation
- Edge cases → document or handle
- Performance → benchmark if critical path

### D. Reversibility Check
Before committing, ask: "Can this be undone?"
- Database migrations → need rollback plan
- File deletions → confirm with user
- API changes → version or deprecate

## How to Use This Skill

1. **Load the skill** at the start of any coding task
2. **Follow the phases** — don't skip ahead
3. **Use checkpoints** as natural pause points
4. **Adjust thoroughness** based on task size (see Decision Matrix)
5. **Report honestly** — if something went wrong, say so

## Anti-Patterns to Avoid

- ❌ Jumping straight to coding without understanding
- ❌ Writing 500+ lines without a checkpoint
- ❌ Assuming the user's intent without asking
- ❌ Skipping tests because "it's simple"
- ❌ Marking done without running checks
- ❌ Over-engineering for hypothetical future needs

## Example Interaction

```
User: "Add authentication to the API"

PHASE 1 — CLARIFY:
AI: "Before I start, a few questions:
  1. JWT or session-based auth?
  2. Should I add user registration too, or just login?
  3. Which auth library do you prefer?
  4. Is this for a new project or existing codebase?"

User: "JWT, login only, use passport.js, existing Express project"

AI: "Got it. I'll add JWT auth with passport.js to your existing Express API.
  Plan: 1) Install deps, 2) Create auth middleware, 3) Add login endpoint,
  4) Add route protection. Proceed?"

User: "Yes"

PHASE 2 — PLAN:
AI: [Shows brief implementation plan]

PHASE 3 — EXECUTE:
AI: [Writes code with micro-checkpoints every ~50 lines]
  Midpoint: "Auth middleware done. Now adding login endpoint..."

PHASE 4 — VERIFY:
AI: "All done. Created 2 files, modified 3. Tests pass.
  Login endpoint: POST /api/auth/login
  Protected routes: use authMiddleware
  Any adjustments needed?"
```

## Metrics (Self-Measurement)

Track these after each task to measure improvement:
- Number of clarifying questions asked vs assumptions made
- Times you paused to re-check your plan
- Bugs caught at checkpoint vs bugs found by user
- Code rewrites needed after user feedback

## Version

v1.0.0 — Initial release
