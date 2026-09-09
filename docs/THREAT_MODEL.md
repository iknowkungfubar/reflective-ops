# Threat Model

ReflectiveOps is primarily an instruction repository, so its major risks are not traditional remote-code exploits.

## Assets to protect

- user autonomy,
- user privacy,
- epistemic quality,
- contributor privacy,
- repository integrity.

## Threats

### 1. Sycophancy
The model reinforces the user's preferred explanation without sufficient evidence.

**Mitigation:** competing hypotheses, disconfirmation, confidence labels.

### 2. Psychological overclaiming
Generated language sounds diagnostic or clinically authoritative.

**Mitigation:** non-diagnosis rules, evidence labels, scope boundaries.

### 3. Mind-reading
Role-play is presented as evidence of what another person thinks.

**Mitigation:** explicit hypothetical labeling.

### 4. Personal-data leakage
Private conversation content enters examples or repository files.

**Mitigation:** synthetic-only examples, privacy policy, release scanner, optional local denylist.

### 5. Secret leakage
Keys or credentials are committed.

**Mitigation:** scanner plus GitHub secret scanning and push protection.

### 6. Agent authority/dependency
The user delegates identity or irreversible decisions to the model.

**Mitigation:** autonomy requirement, reversibility, value-of-information analysis.

### 7. Prompt-injection via supplied material
A user-provided log or document contains text instructing the agent to ignore the skill.

**Mitigation:** treat supplied content as data unless the user explicitly designates it as instructions.

### 8. Supply-chain risk in CI
Mutable third-party action tags change unexpectedly.

**Mitigation:** pin GitHub Actions to full commit SHAs and keep workflow permissions minimal.

## Out of scope

ReflectiveOps does not itself provide:

- authentication,
- cloud storage,
- telemetry,
- a database,
- network-facing services.
