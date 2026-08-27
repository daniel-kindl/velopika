<!-- ste-class: ste-strict -->
# Velopika

Velopika is a personal Chromium-based browser project.
Chromium supplies the web engine and primary browser infrastructure.
Velopika keeps product code in a small product-owned layer.

## Current state

The repository bootstrap is complete on the bootstrap branch.
The repository does not contain Chromium source code.
The next engineering task fetches and builds the pinned Chromium revision.

## First platform

Velopika first supports Windows 10 and Windows 11 on x64 Intel or AMD PCs.
The primary development host is Windows.
A Windows 10 virtual machine is part of the test matrix.

## Project documents

- [Project baseline](docs/PROJECT.md)
- [Language and STE Policy](docs/language/STE.md)
- [Windows build procedure](docs/build/windows.md)
- [Source boundary](docs/architecture/source-boundary.md)
- [Contribution procedure](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

## Chromium pin

The file [`chromium.version`](chromium.version) contains the selected Chromium milestone, version, and source revision.
The Velopika product version stays independent from the Chromium milestone.

## License

Velopika-owned source code uses Apache License 2.0.
Chromium and third-party source code keep their applicable licenses.
