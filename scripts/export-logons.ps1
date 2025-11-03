# scripts\export-logons.ps1
# Export failed (4625) and successful (4624) Windows Security logons to text files in the current directory.
# Run PowerShell as Administrator in the project folder.

$failedPath = ".\logs\FailedLogons.txt"
$successPath = ".\logs\SuccessfulLogons.txt"

wevtutil qe Security /q:"*[System[(EventID=4625)]]" /f:text > $failedPath
wevtutil qe Security /q:"*[System[(EventID=4624)]]" /f:text > $successPath

Write-Host "Export complete:"
Write-Host "  Failed: $failedPath"
Write-Host "  Success: $successPath"
