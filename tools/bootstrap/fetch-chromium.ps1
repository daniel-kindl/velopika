[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$SourceRoot = "C:\src\velopika-chromium",
    [switch]$Run
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$pin = Get-Content (Join-Path $repoRoot "chromium.version") -Raw | ConvertFrom-Json

$commands = @(
    "mkdir $SourceRoot",
    "cd $SourceRoot",
    "fetch --git-cache chromium",
    "cd src",
    "git checkout --detach $($pin.revision)",
    "gclient sync -D"
)

Write-Host "Chromium version: $($pin.version)"
Write-Host "Chromium revision: $($pin.revision)"
Write-Host ""
Write-Host "Planned commands:"
$commands | ForEach-Object { Write-Host "  $_" }

if (-not $Run) {
    Write-Host ""
    Write-Host "No source was downloaded. Run this script with -Run to start the fetch."
    exit 0
}

& (Join-Path $PSScriptRoot "check-windows.ps1") -SourceRoot $SourceRoot
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if (Test-Path $SourceRoot) {
    $items = Get-ChildItem -Force $SourceRoot -ErrorAction SilentlyContinue
    if ($items.Count -gt 0) {
        throw "The source directory is not empty: $SourceRoot"
    }
} else {
    New-Item -ItemType Directory -Path $SourceRoot | Out-Null
}

Push-Location $SourceRoot
try {
    & fetch --git-cache chromium
    if ($LASTEXITCODE -ne 0) { throw "fetch failed with exit code $LASTEXITCODE" }

    Push-Location (Join-Path $SourceRoot "src")
    try {
        & git checkout --detach $pin.revision
        if ($LASTEXITCODE -ne 0) { throw "git checkout failed with exit code $LASTEXITCODE" }

        & gclient sync -D
        if ($LASTEXITCODE -ne 0) { throw "gclient sync failed with exit code $LASTEXITCODE" }

        $actual = (& git rev-parse HEAD).Trim()
        if ($actual -ne $pin.revision) {
            throw "The checkout revision is $actual, but the project pin is $($pin.revision)."
        }
    } finally {
        Pop-Location
    }
} finally {
    Pop-Location
}

Write-Host "The Chromium checkout is ready for GN generation and the first stock build."
