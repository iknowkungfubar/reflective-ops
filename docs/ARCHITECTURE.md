# Architecture

ReflectiveOps is intentionally lightweight.

## Logical architecture

```text
User concern
    |
    v
life-systems-orchestrator
    |
    +--> clarity ---------> baseline-mapper
    +--> behavior --------> behavior-forensics
    +--> belief ----------> belief-reality-auditor
    +--> relationship ----> conflict-perspective-lab
    +--> identity --------> identity-transition-cartographer
    +--> decision --------> decision-lab
    +--> adversity -------> adversity-debrief
    +--> ambivalence -----> change-readiness-interviewer
    +--> execution -------> behavior-change-engineer
    +--> uncertainty -----> experiment-designer
    +--> results ---------> review-calibration
```

## Closed-loop operating model

```text
Observe
  ↓
Separate facts / stories
  ↓
Generate competing hypotheses
  ↓
Choose discriminating evidence
  ↓
Design smallest safe test
  ↓
Act
  ↓
Measure
  ↓
Calibrate
  └───────────────→ repeat
```

## Progressive disclosure

Agents should not load every skill for every request.

Recommended loading sequence:

1. skill names and descriptions for discovery,
2. one selected `SKILL.md`,
3. optional shared reference material only if needed,
4. a template only when producing that artifact.

This keeps context smaller and reduces instruction interference.

## State

ReflectiveOps does not require persistent memory.

If a client supports state, store only the minimum needed for the user's chosen workflow:

- current target,
- observations,
- active hypotheses,
- experiment definitions,
- measurements,
- next review trigger.

Do not persist sensitive personal information merely because persistence is available.

See `core/STATE_SCHEMA.yaml`.
