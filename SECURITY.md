# Security Policy

## Scope

This repository contains specifications and profiles. It does not contain a
production service or private key material.

Security reports are relevant when they concern:

- a cross-subject trust or authorization bypass described by a specification;
- a signature, freshness or revocation rule that can produce a false valid
  result;
- a broken link or example that discloses private material;
- a publication process that could expose credentials or private deployment
  information.

## Reporting

Do not open a public issue for a suspected vulnerability or exposed secret.

Use the repository's **Security → Report a vulnerability** flow. If GitHub
private vulnerability reporting is unavailable, contact maintainer
[@wwumit](https://github.com/wwumit) through GitHub to arrange a private
channel.

Please include:

- the affected document and section;
- the violated invariant;
- a minimal scenario or counterexample;
- whether the issue affects a draft, an implementation, or both.

## Publication boundary

- Private keys, tokens, session cookies and production configuration are not
  accepted in this repository or its history.
- Example credentials MUST be clearly non-production.
- Reporters should avoid including personal data or live action payloads.
