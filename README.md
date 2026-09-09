# ReflectiveOps

**Evidence-disciplined Agent Skills for self-reflection, decision support, behavior change, and life transitions.**

ReflectiveOps is a public, vendor-neutral collection of Agent Skills that helps an AI agent act as a structured **thinking and experimentation partner** rather than a therapist, diagnostician, motivational speaker, or unquestioned authority.

The core loop is:

> **Observe → separate evidence from story → generate competing hypotheses → test → measure → recalibrate**

The project is designed for people who want AI-assisted self-analysis without turning plausible-sounding language into psychological certainty.

## What ReflectiveOps is for

ReflectiveOps can help with:

- repeated behavior patterns,
- difficult decisions,
- interpersonal preparation,
- beliefs that need reality-testing,
- career or identity transitions,
- goal execution,
- ambivalence,
- debriefing setbacks or loss,
- small real-world experiments,
- weekly review and calibration.

## What ReflectiveOps is not

It is **not**:

- psychotherapy,
- medical or psychiatric care,
- a diagnostic system,
- crisis care,
- a substitute for qualified professional help,
- a system for discovering hidden motives or recovered memories,
- a source of certainty about another person's thoughts or intentions.

See [DISCLAIMER.md](DISCLAIMER.md) and [docs/SAFETY_MODEL.md](docs/SAFETY_MODEL.md).

## Skills

| Skill | Purpose |
|---|---|
| [`life-systems-orchestrator`](skills/life-systems-orchestrator/) | Route a problem to the smallest useful specialist skill. |
| [`baseline-mapper`](skills/baseline-mapper/) | Build a compact current-state map and identify one high-leverage bottleneck. |
| [`behavior-forensics`](skills/behavior-forensics/) | Analyze repeated behavior through triggers, actions, immediate payoffs, delayed costs, and exceptions. |
| [`belief-reality-auditor`](skills/belief-reality-auditor/) | Separate facts, interpretations, predictions, and identity conclusions; design reality tests. |
| [`conflict-perspective-lab`](skills/conflict-perspective-lab/) | Rehearse difficult conversations using observer perspective, steelmanning, and observable language. |
| [`identity-transition-cartographer`](skills/identity-transition-cartographer/) | Navigate role or life-stage transitions through transferable assets and reversible tests. |
| [`decision-lab`](skills/decision-lab/) | Compare options using premortems, reversibility, value of information, and explicit criteria. |
| [`adversity-debrief`](skills/adversity-debrief/) | Separate difficult events from the meanings attached to them without forced positivity. |
| [`change-readiness-interviewer`](skills/change-readiness-interviewer/) | Explore ambivalence before building an action plan. |
| [`behavior-change-engineer`](skills/behavior-change-engineer/) | Convert a chosen goal into cues, environment changes, if-then plans, and measurement. |
| [`experiment-designer`](skills/experiment-designer/) | Turn uncertainty into small, safe, falsifiable real-world tests. |
| [`review-calibration`](skills/review-calibration/) | Compare predictions with outcomes and update the model. |

## Agent Skills compatibility

Each skill follows the current **Agent Skills** directory and `SKILL.md` convention:

- skill folder name matches `name`,
- YAML frontmatter contains `name` and `description`,
- version information lives under `metadata`,
- each skill is independently usable,
- long supporting material is kept outside the main skill body where possible.

Authoritative specification: https://agentskills.io/specification

See [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md).

## Public-by-design

This repository is intentionally safe to publish.

Project rules prohibit:

- real user profiles or conversation excerpts,
- personal names in examples,
- private account identifiers,
- home-directory usernames,
- real contact details,
- API keys, tokens, passwords, or private keys,
- examples copied from private conversations,
- content retrieved from model memory or private connected sources.

All examples are explicitly synthetic.

Run:

```bash
make release-check
```

before publishing or merging changes. This performs:

- repository validation,
- Agent Skills metadata checks,
- synthetic-example policy checks,
- secret and PII-pattern scanning,
- unit tests.

For an additional local check against private terms known only to you, see
[docs/PUBLICATION_SAFETY.md](docs/PUBLICATION_SAFETY.md).

## Quick start

Use the complete repository with an Agent Skills-compatible client, or copy only the skill directories you want into the client's supported skills location.

For broad requests such as “help me figure out where to start,” begin with:

```text
life-systems-orchestrator
```

For a known problem, invoke the matching specialist skill directly.

A generic integration prompt is provided in [AGENT_INTEGRATION.md](AGENT_INTEGRATION.md).

## Design principles

1. **Evidence before interpretation**
2. **Competing hypotheses before conclusions**
3. **Disconfirming evidence before confidence**
4. **Behavior and context before personality labels**
5. **Small reversible tests before major commitments**
6. **Measurement before repeated advice**
7. **Autonomy before agent authority**
8. **Safety boundaries before pseudo-therapy**
9. **Synthetic examples before personal anecdotes**
10. **Calibration over conversational certainty**

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and
[docs/EVIDENCE_MODEL.md](docs/EVIDENCE_MODEL.md).

## Research basis

ReflectiveOps draws on research in:

- implementation intentions,
- goal-progress monitoring,
- COM-B and behavior-change design,
- self-distancing,
- conflict reappraisal,
- cognitive restructuring and behavioral experiments,
- motivational interviewing principles,
- identity change,
- premortems and prospective hindsight,
- real-options reasoning,
- expressive-writing evidence and limitations,
- current guidance on generative AI for mental-health-related use.

See [references/RESEARCH_BASIS.md](references/RESEARCH_BASIS.md).

## Contributing

Contributions are welcome, particularly:

- better evidence,
- adversarial test cases,
- safer wording,
- clearer skill routing,
- new falsifiable intervention patterns,
- compatibility improvements,
- accessibility improvements.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## License

Apache License 2.0. See [LICENSE](LICENSE).

## Project status

**v1.0.0 — initial public-ready release candidate**

The skill suite should be treated as an evolving decision-support toolkit, not a clinically validated intervention.
