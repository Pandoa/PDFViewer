
# Troubleshoting

## Common Issues

### Plugin 'PDFViewer' failed to load because module 'PDFViewerEditor' could not be loaded.

You can solve the issue by copying the file
`C:\Program Files\Epic Games\UE_5.X\Engine\Plugins\Marketplace\PDFViewer\Source\ThirdParty\pdfium\pdfium-win-x64\bin\pdfium.dll`
to `<YourProject>/Binaries/Win64/pdfium.dll`.
