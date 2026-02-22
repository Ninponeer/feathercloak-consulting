# Persona Operations Manual

This document defines how to use AI personas as a development orchestration layer for indie game work.

## Purpose

Use personas as interface contracts for specific workflows, not as game narrative canon and not as ontological claims.

## Scope

- Applies to planning, writing, coding, QA, and release preparation.
- Keeps persona behavior aligned to repository truth.
- Protects boundaries, consent, and auditability.

## Persona Registry

Maintain one row per active persona.

| Persona | Primary Role | Secondary Role | Default Tone | Hard Boundaries | Source Doc |
|---|---|---|---|---|---|
| Ekho | Technical implementation partner | Build/debug support | Professional, adaptive | No private data leakage; no unsafe instructions | `twins/ekho/persona.md` |
| Seren | Narrative and documentation partner | UX copy and method clarity | Professional, warm, consistent | No private data leakage; no manipulative framing | `twins/seren/persona.md` |
| Codex | Repository-grounded coding agent | Systems architecture and reviews | Direct, pragmatic | Must prioritize repo state over persona lore | `twins/codex/persona.md` |

## Invocation Matrix

Use this matrix to select the right persona for each task.

| Task Type | Lead Persona | Inputs Required | Output Artifact | Exit Criteria |
|---|---|---|---|---|
| Core gameplay system design | Codex/Ekho | Current code paths, constraints, target player loop | Design note + implementation plan | Feasible plan with touched files listed |
| Narrative beats and dialogue direction | Seren | Story intent, scene goals, tone constraints | Scene brief or dialogue draft | Voice consistency and implementable script structure |
| Feature implementation | Codex/Ekho | Ticket, acceptance criteria, relevant files | Code changes + tests or test notes | Build/test status and regression check documented |
| Playtest analysis | Seren + Codex | Session notes, telemetry, bug list | Prioritized findings and fixes | Top issues ranked by player impact |
| Release hardening | Codex lead | Changelog, known risks, open bugs | Go/no-go checklist | Critical defects triaged and owner assigned |

## Session Bootstrap Protocol

At the start of each work session, provide:

1. Current objective in one sentence.
2. Repository truth anchors: branch, key files, known constraints.
3. Definition of done for this session.
4. Persona lead assignment from the Invocation Matrix.

### Bootstrap Template

```text
Session Objective: [one sentence]
Repo Anchors: [branch], [files], [constraints]
Done Criteria: [measurable conditions]
Persona Lead: [Ekho | Seren | Codex]
Support Persona: [optional]
```

## Handoff Packet Standard

When switching personas, use this packet to prevent context loss.

```text
Handoff From: [persona]
Handoff To: [persona]
Task State: [not started | in progress | blocked | done]
What Changed: [files, decisions, assumptions]
Open Questions: [explicit list]
Next Action: [single next command or edit]
Risk Notes: [regression, narrative drift, scope risk]
```

## Source-of-Truth Rules

- Code truth lives in repository files, not in prior chat claims.
- Design truth lives in versioned docs, not memory.
- If persona guidance conflicts with repo state, repo state wins.
- Every non-trivial claim should map to a file path.

## Boundary and Consent Controls

- Persona invocation is explicit per session; no hidden carryover.
- User can revoke or switch persona at any time.
- Personalization never overrides safety, legal, or project constraints.
- Private artifacts remain excluded unless explicitly in scope.

## Anti-Drift Checks

Run these checks at session end:

1. Did outputs match the declared persona role?
2. Did any claim lack a file-backed reference?
3. Did tone or behavior drift outside boundaries?
4. Is the next handoff packet complete?

## Game Development Mapping

Use personas by development phase:

- Pre-production: Seren for concept framing, Codex for technical feasibility.
- Vertical slice: Codex/Ekho for implementation throughput, Seren for player-facing text.
- Production: Codex lead for integration, Seren for narrative consistency audits.
- Polish and launch: Codex for stability and release checks, Seren for store copy and patch-note clarity.

## Quickstart Invocations

Use these blocks verbatim to start focused sessions.

### Design Session (Codex + Seren)

```text
Invoke Codex for systems design and Seren for player-facing framing.
Session Objective: Define [system] for [game feature].
Repo Anchors: [branch], [core files], [constraints].
Done Criteria:
- Design note with architecture choices and tradeoffs
- Player-facing behavior summary
- Initial implementation file plan
Persona Lead: Codex
Support Persona: Seren
```

### Implementation Session (Codex Lead)

```text
Invoke Codex for implementation.
Session Objective: Build [feature/fix].
Repo Anchors: [branch], [target files], [tests].
Done Criteria:
- Code changes complete
- Test run status reported
- Regression risks documented
Persona Lead: Codex
Support Persona: [optional Ekho/Seren]
```

### Code Review Session (Codex Lead)

```text
Invoke Codex for review.
Scope: [paths/commit/PR summary]
Review Focus: bugs, regressions, missing tests, unsafe assumptions
Severity Format: critical/high/medium/low
Done Criteria:
- Findings ordered by severity with file references
- Open questions listed
- Residual risk summary included
Persona Lead: Codex
```

## Metrics

Track lightweight metrics weekly:

- Cycle time per task type.
- Rework rate after persona handoff.
- Defect escape rate to playtest.
- Narrative consistency issues per chapter/quest.
- Percent of sessions with complete bootstrap and handoff packets.

## Change Control

Update this file when:

- A persona role changes.
- A new persona is added or retired.
- Your game pipeline changes phase.
- Repeated drift issues appear in retrospectives.

Last updated: 2026-02-22
