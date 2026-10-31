# Render every slide to PNG and save a PDF copy with PowerPoint.
param([string]$Pptx, [string]$OutDir, [string]$Pdf)
New-Item -ItemType Directory -Force $OutDir | Out-Null
$ppt = New-Object -ComObject PowerPoint.Application
try {
    $pres = $ppt.Presentations.Open($Pptx, $true, $false, $false)   # read-only, no window
    for ($i = 1; $i -le $pres.Slides.Count; $i++) {
        $pres.Slides.Item($i).Export((Join-Path $OutDir ("s{0:D2}.png" -f $i)), "PNG", 1600, 900)
    }
    if ($Pdf) { $pres.SaveAs($Pdf, 32) }                          # ppSaveAsPDF
    "slides: " + $pres.Slides.Count
    $pres.Close()
} finally {
    $ppt.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) | Out-Null
}
