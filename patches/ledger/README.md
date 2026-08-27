<!-- ste-class: ste-strict -->
# Chromium patch ledger

Create one ledger record for each durable Velopika integration point in Chromium source.
Do not create a ledger entry before the related source change exists.

Each record must contain:

- Patch ID
- Subsystem
- Purpose
- Chromium touchpoints
- Velopika touchpoints
- Security impact
- Test coverage
- Upstream status
- Removal condition
- Chromium revision.

Copy `TEMPLATE.yaml` for a new record.
