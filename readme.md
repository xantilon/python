---
Author: Edgar Holzke
Create date: 02.04.2022
---

# Purpose

Write EXE file without dependencies to merge two or more PDF files 

This can replace a .Net library with the same purpose. Just deploy this EXE instead


# Usage

```
.\pdfmerge.exe merged.pdf .\test\gematik.pdf .\test\trumans.pdf .\test\det.pdf .\test\anton.pdf
```

```csharp
System.Diagnostics.Process p = new();
p.StartInfo.UseShellExecute = false;
p.StartInfo.CreateNoWindow = true;
p.StartInfo.RedirectStandardOutput = true;
int codepage = System.Globalization.CultureInfo.CurrentCulture.TextInfo.OEMCodePage;
System.Text.Encoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);
p.StartInfo.StandardOutputEncoding = System.Text.Encoding.GetEncoding(codepage);
p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
p.StartInfo.FileName = "pdfmerge.exe";
p.StartInfo.Arguments = @"merged.pdf .\test\gematik.pdf .\test\trumans.pdf .\test\det.pdf .\test\anton.pdf";
p.Start();
var output = p.StandardOutput.ReadToEnd().Split("\r\n");
p.WaitForExit();


```