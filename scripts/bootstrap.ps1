# Downloads portable tools (no admin). Run from the project root. Untested on a clean machine: report problems in docs/GOTCHAS.md.
$ErrorActionPreference = "Stop"
$root = (Get-Location).Path
New-Item -ItemType Directory -Force "$root\tools\blender-dl" | Out-Null
$zip = "$root\tools\blender-dl\blender-4.5.15-windows-x64.zip"
if (-not (Test-Path $zip)) {
  Invoke-WebRequest "https://download.blender.org/release/Blender4.5/blender-4.5.15-windows-x64.zip" -OutFile $zip
}
if (-not (Test-Path "$root\tools\blender-4.5.15-windows-x64")) {
  Expand-Archive $zip -DestinationPath "$root\tools"
}
# Python analysis environment
python -m venv "$root\tools\py-extras"
& "$root\tools\py-extras\Scripts\python.exe" -m pip install librosa scenedetect[opencv] pyloudnorm soundfile numpy scipy
Write-Host "Done. Audacity portable: download manually from https://www.audacityteam.org/download/ if wanted."
