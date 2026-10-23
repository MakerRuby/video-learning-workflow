# Video Learning Workflow - project initialization
# Bootstraps starter documents into a project and merges a short memory block
# into AGENTS.md, CLAUDE.md, and CODEBUDDY.md so that future sessions in that
# workspace (Codex, Claude Code, WorkBuddy) load the skill automatically.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File scripts/init_project.ps1 [-ProjectRoot <path>] [-Force]
#   Default ProjectRoot is the current directory.
#   -Force backs up any existing non-memory file to <name>.bak-<timestamp> before
#   replacing it; without it, existing files are left untouched. Memory files are
#   merged in place between the workflow markers (or appended if not present).

param(
  [string]$ProjectRoot = (Get-Location).Path,
  [switch]$Force
)

$ErrorActionPreference = 'Stop'

# Resolve the skill root by walking upward to the folder that contains SKILL.md.
# Works whether the skill folder is installed, symlinked, or extracted from the zip.
$SkillRoot = Split-Path -Parent $PSScriptRoot
$Probe = $SkillRoot
while ($Probe -and -not (Test-Path -LiteralPath (Join-Path $Probe 'SKILL.md'))) { $Probe = Split-Path -Parent $Probe }
if (-not $Probe) { throw "Cannot locate SKILL.md above $SkillRoot" }
$SkillRoot = (Resolve-Path -LiteralPath $Probe).Path
$TemplateDir = Join-Path $SkillRoot 'assets\project-starter'

if (-not (Test-Path -LiteralPath $TemplateDir)) {
  throw "Starter templates not found under skill folder: $TemplateDir"
}
if (-not (Test-Path -LiteralPath $ProjectRoot)) {
  throw "Project root not found: $ProjectRoot"
}

$MemoryNames = @('AGENTS.md','CLAUDE.md','CODEBUDDY.md')
$StartMark = '<!-- video-learning-workflow:start -->'
$EndMark = '<!-- video-learning-workflow:end -->'
$created = [System.Collections.Generic.List[string]]::new()
$merged  = [System.Collections.Generic.List[string]]::new()
$skipped = [System.Collections.Generic.List[string]]::new()
$backed  = [System.Collections.Generic.List[string]]::new()

Get-ChildItem -LiteralPath $TemplateDir -File | Sort-Object Name | ForEach-Object {
  $name = $_.Name
  $dst = Join-Path $ProjectRoot $name
  $templateText = (Get-Content -Raw -LiteralPath $_.FullName).Replace('__SKILL_ROOT__', $SkillRoot)

  if ($MemoryNames -contains $name) {
    # Extract the marker block and merge it into the project memory file.
    $start = $templateText.IndexOf($StartMark)
    $end = $templateText.IndexOf($EndMark)
    if ($start -lt 0 -or $end -lt 0) { throw "Memory template $name is missing the workflow markers" }
    $block = $templateText.Substring($start, $end - $start + $EndMark.Length).Trim()

    if (Test-Path -LiteralPath $dst) {
      $current = Get-Content -Raw -LiteralPath $dst
      $cs = $current.IndexOf($StartMark)
      $ce = $current.IndexOf($EndMark)
      if ($cs -ge 0 -and $ce -gt $cs) {
        $updated = $current.Substring(0, $cs) + $block + $current.Substring($ce + $EndMark.Length)
      } else {
        if ($current -and -not $current.EndsWith("`n")) { $current += "`n" }
        $updated = $current + "`n" + $block + "`n"
      }
      Set-Content -LiteralPath $dst -Value $updated -Encoding UTF8 -NoNewline
      $merged.Add($name)
    } else {
      Set-Content -LiteralPath $dst -Value $templateText -Encoding UTF8 -NoNewline
      $created.Add($name)
    }
    return
  }

  if (Test-Path -LiteralPath $dst) {
    if ($Force) {
      $bak = "$dst.bak-$(Get-Date -Format 'yyyyMMddHHmmss')"
      Copy-Item -LiteralPath $dst -Destination $bak
      $backed.Add($bak)
      Set-Content -LiteralPath $dst -Value $templateText -Encoding UTF8 -NoNewline
      $created.Add($name)
    } else {
      $skipped.Add($name)
    }
  } else {
    Set-Content -LiteralPath $dst -Value $templateText -Encoding UTF8 -NoNewline
    $created.Add($name)
  }
}

Write-Output "Project initialized: $ProjectRoot"
Write-Output "Created: $($created -join ', ')"
if ($merged.Count -gt 0) { Write-Output "Memory blocks merged: $($merged -join ', ')" }
if ($skipped.Count -gt 0) { Write-Output "Skipped (already exists, use -Force to replace): $($skipped -join ', ')" }
if ($backed.Count -gt 0)  { Write-Output "Backups: $($backed -join ', ')" }
Write-Output "Memory files updated (AGENTS.md, CLAUDE.md, CODEBUDDY.md): future sessions in this workspace will load the skill automatically."
