<!-- ste-class: ste-strict -->
# Velopika source boundary

Chromium is inherited infrastructure.
Velopika keeps product decisions in product-owned code when Chromium architecture permits this separation.

Use this source direction:

```text
Chromium upstream
       |
small integration points
       |
Velopika core
       |
Velopika experience
```

Reserve `//velopika/` for product-owned browser code after the Chromium checkout exists.
Do not create substitute Chromium source files in this repository.

Use small named adapters when Velopika must connect to Chromium internals.
Do not combine a product function with an unrelated Chromium refactor.
Record each durable integration point in `patches/ledger/`.

Do not replace Blink, V8, the network service, the sandbox, or the Chromium process model.
Do not weaken site isolation, certificate verification, or renderer protections for product convenience.

A source search for `Velopika` must find product behavior, related tests, and design records.
Do not hide Velopika behavior in unrelated Chromium files.
