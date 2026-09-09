# Architecture

ReflectiveOps is intentionally lightweight.

## Logical architecture

```text
User concern
    |
    v
guided-self-improvement-journey (optional broad-request workflow)
    |
    +--> orientation / interview
    |       |
    |       v
    |   life-systems-orchestrator
    |       |
    |       +--> clarity ---------> baseline-mapper
    |       +--> behavior --------> behavior-forensics
    |       +--> belief ----------> belief-reality-auditor
    |       +--> relationship ----> conflict-perspective-lab
    |       +--> identity --------> identity-transition-cartographer
    |       +--> decision --------> decision-lab
    |       +--> adversity -------> adversity-debrief
    |       +--> ambivalence -----> change-readiness-interviewer
    |       +--> execution -------> behavior-change-engineer
    |       +--> uncertainty -----> experiment-designer
    |       +--> results ---------> review-calibration
    |       |
    |       v
    |   evidence model → user checkpoint → action/experiment → report
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
2. `guided-self-improvement-journey/SKILL.md` for a broad request,
3. one selected specialist `SKILL.md`,
4. optional shared reference material only if needed,
5. a template only when producing that artifact.

This keeps context smaller and reduces instruction interference.

## Report presentation

The guided journey treats `templates/FINAL_REPORT.md` as the portable report contract. When a client can create files, the same structured content can be presented with `templates/final-report.html` and `templates/final-report.css`. The HTML/CSS is a dependency-free presentation layer, not a runtime workflow engine; no client is assumed to support HTML generation. Reports may contain sensitive personal material and should remain private by default.

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
