[CmdletBinding()]
param(
    [string]$SourceRoot = "C:\src\velopika-chromium",
    [int]$MinimumFreeGb = 100
)

$ErrorActionPreference = "Stop"
$failures = New-Object System.Collections.Generic.List[string]

function Write-Result {
    param([string]$Name, [bool]$Ok, [string]$Detail)
    $state = if ($Ok) { "PASS" } else { "FAIL" }
    Write-Host ("{0,-6} {1}: {2}" -f $state, $Name, $Detail)
    if (-not $Ok) { $script:failures.Add(("{0}: {1}" -f $Name, $Detail)) }
}

$isWindows = $env:OS -eq "Windows_NT"
Write-Result "Windows" $isWindows "Windows 10 or newer is required."

if ($isWindows) {
    $os = [System.Environment]::OSVersion.Version
    Write-Result "OS version" ($os.Major -ge 10) ("Detected {0}." -f $os)
}

Write-Result "Architecture" ([Environment]::Is64BitOperatingSystem) "An x64 operating system is required."

$driveName = [System.IO.Path]::GetPathRoot($SourceRoot).TrimEnd('\').TrimEnd(':')
$drive = Get-PSDrive -Name $driveName -ErrorAction SilentlyContinue
if ($null -ne $drive) {
    $freeGb = [math]::Floor($drive.Free / 1GB)
    Write-Result "Disk space" ($freeGb -ge $MinimumFreeGb) ("{0} GB free on {1}:; {2} GB required." -f $freeGb, $driveName, $MinimumFreeGb)
} else {
    Write-Result "Disk space" $false "The source drive was not found."
}

foreach ($command in @("git", "gclient", "fetch", "gn", "autoninja")) {
    $found = Get-Command $command -ErrorAction SilentlyContinue
    $detail = if ($null -ne $found) { $found.Source } else { "Command not found in PATH." }
    Write-Result $command ($null -ne $found) $detail
}

$vswhere = Join-Path ${env:ProgramFiles(x86)} "Microsoft Visual Studio\Installer\vswhere.exe"
if (Test-Path $vswhere) {
    $installation = & $vswhere -latest -products * -format json | ConvertFrom-Json | Select-Object -First 1
    if ($null -ne $installation) {
        $version = [version]$installation.installationVersion
        Write-Result "Visual Studio" ($version.Major -ge 18) ("Detected {0} at {1}." -f $version, $installation.installationPath)
    } else {
        Write-Result "Visual Studio" $false "No Visual Studio installation was found."
    }
} else {
    Write-Result "Visual Studio" $false "vswhere.exe was not found. Install Visual Studio 2026 version 18.0 or newer."
}

$pinPath = Join-Path (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path "chromium.version"
$pin = Get-Content $pinPath -Raw | ConvertFrom-Json
Write-Host "PIN    Chromium $($pin.version)"
Write-Host "PIN    $($pin.revision)"
Write-Host "PATH   Source: $SourceRoot"
Write-Host "PATH   Profile: C:\src\velopika-data\dev"

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "The host has blocking bootstrap results."
    exit 1
}

Write-Host ""
Write-Host "The host passed the automated bootstrap checks."
Write-Host "Verify the Visual Studio components and Windows SDK with the current Chromium Windows instructions."
