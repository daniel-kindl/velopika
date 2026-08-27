<!-- ste-class: ste-strict -->
# Branch and release model

Use Conventional Commits for commit and pull-request titles.
Use the form `type(scope): imperative summary`.

Use this branch flow:

```text
feature/* -> dev -> release/x.y.z -> main
```

Make a feature branch from `dev` for one related change.
Run required checks before you merge the feature branch into `dev`.
A human must approve each merge.

Make `release/x.y.z` from `dev` when the release scope is complete.
Add only fixes, documentation, release metadata, and security work to a release branch.
Merge an approved release branch into `main`.
Make the signed `vX.Y.Z` tag from the approved stable source.

Make `hotfix/x.y.z` from `main` for an urgent stable correction.
Merge the correction into `main`, then merge it into `dev` and each active release branch.

Velopika uses SemVer for product versions.
The Chromium milestone and revision are separate build information.
