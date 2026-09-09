# Security Policy

## Supported versions

Security and privacy fixes are applied to the current release line.

| Version | Supported |
|---|---|
| 1.x | Yes |

## Reporting a vulnerability or privacy leak

Do **not** open a public issue containing:

- credentials,
- private user data,
- sensitive personal information,
- exploit details that would place users at immediate risk.

Use GitHub's **private vulnerability reporting** feature for the repository when available.

If private vulnerability reporting is unavailable, open a public issue containing only a minimal non-sensitive request asking maintainers to enable a private reporting channel. Do not include the sensitive material itself.

## Repository security posture

The project aims to:

- use no runtime dependencies for repository validation,
- avoid telemetry,
- avoid network access from skills,
- keep CI permissions read-only unless a workflow explicitly needs more,
- pin GitHub Actions to full commit SHAs,
- scan for common secret and PII patterns before release,
- avoid `pull_request_target` for validation of untrusted contributions.

## GitHub repository settings recommended for maintainers

For a public repository, enable where available:

- secret scanning,
- push protection,
- dependency alerts,
- private vulnerability reporting,
- branch protection or repository rules requiring CI,
- review before merge.

These settings complement repository checks; they do not replace review.
