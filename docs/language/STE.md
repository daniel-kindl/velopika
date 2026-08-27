<!-- ste-class: ste-strict -->
# Velopika language and STE policy

Use ASD-STE100 Simplified Technical English, Issue 9, as the mandatory baseline for Velopika-owned technical English.
Do not copy the ASD-STE100 controlled dictionary into this repository.
Use an official ASD, ASD-STAN, or STEMG source for the standard.

## Output classes

Use `ste-strict` for technical and engineering text.
The final text must comply with ASD-STE100 Issue 9.

Use `ste-humanized` for text that a product user reads.
Write and validate a correct STE baseline before Claude `/humanizer` processes the text.
The processed user-facing text does not have to stay strict STE.

Use `ste-exempt` only for text that Velopika cannot change or this policy identifies as fixed.
Permitted examples include external quoted text, legal text, license text, protocol strings, programming identifiers, and fixed external logs.
Do not use an exemption only because strict STE is difficult.

## Technical text

Use `ste-strict` for architecture documents, ADRs, build procedures, release procedures, and security documents.
Use `ste-strict` for README files, API documents, developer help, release notes, and code comments.
Use `ste-strict` for issue templates, pull-request templates, and agent instructions.

Use American English spelling unless an official directive requires a different spelling.
Use approved words only with their approved meanings and approved parts of speech.
Use approved project technical nouns and technical verbs when STE rules permit them.
Use the same technical noun for the same item.
Use active voice unless STE permits passive voice because the agent is unknown.
Use approved verb forms and approved tenses only.
Use an `-ing` form only when STE permits it.
Use multi-word nouns of three words or less unless STE Rule 2.2 applies.
Use articles and demonstrative adjectives when clear meaning needs them.
Do not use contractions.

Use a maximum of 20 words in a procedural or safety sentence.
Use a maximum of 25 words in a descriptive sentence or note.
Use one instruction in each procedural sentence unless actions occur at the same time.
Use imperative verbs for procedures.
Do not use imperative verbs in descriptive text or notes.
Use one topic in each descriptive paragraph.
Use a maximum of six sentences in each descriptive paragraph.

## Terminology

Keep approved project terms in `docs/language/terminology.yaml`.
Each term entry must contain the term, type, approved meaning, and subject field.
Use a short technical noun when Velopika can select the term.
Do not use different technical nouns for one project concept.

## User-facing processing

Use this procedure for `ste-humanized` text:

1. Write the required meaning in mandatory STE.
2. Run the STE quality gate.
3. Correct all blocking STE findings.
4. Process the approved text with Claude `/humanizer`.
5. Compare the processed text with the approved baseline.
6. Reject the processed text when technical meaning or required behavior changes.

The `/humanizer` step can change tone and usual user wording.
It must keep technical meaning, safety information, limits, security meaning, and product behavior.
It must not remove a required action.
Keep the STE baseline with the user-facing text as review and test evidence.

## Quality gate

Use `STE-LINT` for deterministic checks.
Use `STE-REVIEW` for meaning, parts of speech, active voice, technical terms, and sentence construction.
Use `HUMANIZER-REVIEW` for comparison of user-facing text with its approved STE baseline.

A blocking STE finding prevents acceptance.
The deterministic linter does not prove complete ASD-STE100 compliance.
Dictionary validation needs an authorized local source or an applicable STE authoring tool.
Do not publish ASD dictionary data in repository or CI artifacts.
