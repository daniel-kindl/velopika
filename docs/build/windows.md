<!-- ste-class: ste-strict -->
# Windows Chromium build procedure

This procedure prepares the first stock Chromium build for Velopika.
Use a Windows 10 or Windows 11 x64 host.
Do not make a Velopika Chromium source change during this procedure.

## 1. Check the host

1. Open PowerShell from the Velopika repository root.
2. Run `tools\bootstrap\check-windows.ps1`.
3. Correct each blocking result before you continue.

Chromium currently requires Windows 10 or newer and an x86-64 machine.
Chromium requires at least 100 GB of free NTFS disk space.
Chromium currently requires Visual Studio 2026 version 18.0 or newer.
Use the current Chromium Windows instructions to verify the required Visual Studio components and Windows SDK.

Official instructions: <https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md>

## 2. Install depot_tools

1. Make `C:\src` if it does not exist.
2. Clone `depot_tools` to `C:\src\depot_tools`.
3. Put `C:\src\depot_tools` at the start of `PATH`.
4. Set `DEPOT_TOOLS_WIN_TOOLCHAIN=0` when you use the local Visual Studio installation.
5. Run `gclient` from `cmd.exe` one time.
6. Run `where python3`.
7. Make sure that the `depot_tools` Python entry is first.

Use the official Chromium instructions for the current `depot_tools` procedure.

## 3. Read the Chromium pin

Run:

```powershell
Get-Content .\chromium.version
```

The bootstrap pin is:

- Milestone: 152
- Version: 152.0.7977.55
- Revision: `5659715958734a5ca90fda5d3c5249daf2b28c3d`

Do not replace this revision during the first build task without an approved source-update decision.

## 4. Fetch Chromium

Use a source path without spaces.
The recommended path is `C:\src\velopika-chromium`.

Run:

```cmd
cd /d C:\src
mkdir velopika-chromium
cd velopika-chromium
fetch --git-cache chromium
cd src
git checkout --detach 5659715958734a5ca90fda5d3c5249daf2b28c3d
gclient sync -D
```

`fetch --git-cache chromium` keeps repository history and uses a shared cache.
The official Chromium instructions identify this method as a faster full-history checkout.

## 5. Verify the revision

Run:

```cmd
git rev-parse HEAD
```

The result must be:

```text
5659715958734a5ca90fda5d3c5249daf2b28c3d
```

Stop if the revision is different.

## 6. Generate the first build directory

From `C:\src\velopika-chromium\src`, run:

```cmd
gn gen out\Default
```

The default configuration is a debug component build for the host system.
Do not add product build arguments before the stock build succeeds.

## 7. Build Chromium

Run:

```cmd
autoninja -C out\Default chrome
```

Do not continue until the build succeeds.
Record each failure with the exact command and last useful error output.

## 8. Run Chromium with an isolated profile

Make a separate development-data directory.
Then run:

```cmd
mkdir C:\src\velopika-data\dev
out\Default\chrome.exe --user-data-dir=C:\src\velopika-data\dev
```

Do not use an existing Chrome, Chromium, or future Velopika stable profile.

## 9. Record the build result

From the Velopika repository root, run:

```powershell
.\tools\bootstrap\record-build.ps1 `
    -ChromiumSource C:\src\velopika-chromium\src `
    -BuildOutput C:\src\velopika-chromium\src\out\Default
```

The script writes local evidence to `.velopika-local\build-result.json`.
This file is not committed.

## Completion result

The first build task is complete only when stock Chromium builds and starts with the isolated development profile.
Do not add Velopika branding or product functions before this result exists.
