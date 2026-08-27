[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ChromiumSource,
    [Parameter(Mandatory = $true)]
    [string]$BuildOutput
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$pin = Get-Content (Join-Path $repoRoot "chromium.version") -Raw | ConvertFrom-Json

if (-not (Test-Path $ChromiumSource)) { throw "Chromium source path not found: $ChromiumSource" }
if (-not (Test-Path $BuildOutput)) { throw "Build output path not found: $BuildOutput" }

$actual = (& git -C $ChromiumSource rev-parse HEAD).Trim()
$chromePath = Join-Path $BuildOutput "chrome.exe"

$result = [ordered]@{
    recorded_at = (Get-Date).ToUniversalTime().ToString("o")
    expected_revision = $pin.revision
    actual_revision = $actual
    revision_matches = ($actual -eq $pin.revision)
    chromium_version = $pin.version
    chromium_source = $ChromiumSource
    build_output = $BuildOutput
    chrome_exists = (Test-Path $chromePath)
    chrome_path = $chromePath
    host_os = [System.Environment]::OSVersion.VersionString
    host_x64 = [Environment]::Is64BitOperatingSystem
}

$localDir = Join-Path $repoRoot ".velopika-local"
New-Item -ItemType Directory -Force -Path $localDir | Out-Null
$outPath = Join-Path $localDir "build-result.json"
$result | ConvertTo-Json -Depth 4 | Set-Content -Encoding utf8 $outPath

Write-Host "Build evidence: $outPath"
if (-not $result.revision_matches) { throw "The Chromium revision does not match the project pin." }
if (-not $result.chrome_exists) { throw "chrome.exe was not found in the build output." }
