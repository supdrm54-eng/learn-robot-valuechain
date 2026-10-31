# Open the textbook HTML in Word, embed linked pictures, save as DOCX and PDF.
param([string]$Html, [string]$Docx, [string]$Pdf, [string[]]$Pics)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($Html, $false, $true)
    # Replace each linked picture with an embedded copy at the same spot.
    # Pictures appear in document order, matching $Pics order.
    $shapes = @($doc.InlineShapes)
    for ($i = 0; $i -lt $shapes.Count -and $i -lt $Pics.Count; $i++) {
        $s = $shapes[$i]
        $src = $Pics[$i]
        if (Test-Path $src) {
            $rng = $s.Range
            $w = $s.Width; $h = $s.Height
            $s.Delete()
            $pic = $doc.InlineShapes.AddPicture($src, $false, $true, $rng)
            $pic.LockAspectRatio = -1
            $pic.Width = [Math]::Min($w, 450)
        }
    }
    $doc.PageSetup.PaperSize = 7          # wdPaperA4
    $doc.SaveAs2([ref]$Docx, [ref]16)     # wdFormatDocumentDefault
    $doc.Close([ref]0)
    $doc2 = $word.Documents.Open($Docx, $false, $true)
    $word.ActiveWindow.View.Type = 3      # wdPrintView
    $doc2.ExportAsFixedFormat($Pdf, 17)   # wdExportFormatPDF
    "pages: " + $doc2.ComputeStatistics(2)
    $linked = 0
    foreach ($s in @($doc2.InlineShapes)) { try { if ($s.LinkFormat.SourceFullName) { $linked++ } } catch {} }
    "pictures: " + $doc2.InlineShapes.Count + " (still linked: " + $linked + ")"
    "tables: " + $doc2.Tables.Count
    $doc2.Close([ref]0)
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}
