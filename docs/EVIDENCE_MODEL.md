# Evidence Model

ReflectiveOps uses explicit evidence categories to prevent generated explanations from becoming accidental facts.

## Categories

### OBSERVATION
A concrete event or behavior described as having occurred.

### MEASURE
A number, frequency, duration, date, count, or recorded outcome.

### REPORT
Information attributed to another source or person.

### INTERPRETATION
Meaning assigned to an event.

### HYPOTHESIS
A testable explanation.

### PREDICTION
A future observation expected if a hypothesis is correct.

### UNKNOWN
Important information not yet established.

## Evidence ladder

As a rough default:

1. repeated directly observed behavior or measured outcomes,
2. multiple independent credible reports,
3. one concrete example,
4. retrospective impression,
5. inference,
6. generated intuition.

This is a heuristic, not a universal scientific hierarchy.

## Confidence labels

Use:

- **low**
- **medium**
- **high**

Always include a short reason.

Avoid pseudo-precision such as `82.4% confidence` unless a real calibrated model or empirical frequency justifies it.

## Competing-hypothesis rule

For material conclusions:

1. state the leading hypothesis,
2. generate at least one credible alternative,
3. identify discriminating evidence,
4. state what would reduce confidence.

## Disconfirmation rule

A useful hypothesis should be able to lose.

If no imaginable observation could weaken it, treat it as a narrative or value statement rather than an empirical explanation.
