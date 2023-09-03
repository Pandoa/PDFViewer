# `UPDFPage`

## Functions

### `GetWidth`
- Gets the width of the page. The width is measured in typographic points. In typography, one point equals to 1/72 inch, which is about 0.35 millimeter.
- return The width of the page.
```cpp
double GetWidth() const;
```

### `GetHeight`
- Gets the height of the page. The height is measured in typographic points. In typography, one point equals to 1/72 inch, which is about 0.35 millimeter.
- return The height of the page.
```cpp
double GetHeight() const;
```

### `RenderPageSync`
- Renders the page to a texture.
- param Start The start position to render the page.
- param Size The size of the rendered page in pixel.
- param Orientation The orientation of the page.
- param Flags Optional flags for the rendering.
- return A texture object containing the render of the page.
```cpp
class UTexture2D* RenderPageSync(FPDFVector2D Start, FPDFVector2D Size, FLinearColor BackgroundColor, EPDFPageOrientation Orientation, const TSet<EPDFFlags>& Flags);
```

### `RenderPageBitmapSync`
- Renders the page to a binary buffer.
- param Start The start position to render the page.
- param Size The size of the rendered page in pixel.
- param Orientation The orientation of the page.
- param Flags Optional flags for the rendering.
- return Bitmap data of the rendered page.
```cpp
TArray<uint8> RenderPageBitmapSync(FPDFVector2D Start, FPDFVector2D Size, FLinearColor BackgroundColor, EPDFPageOrientation Orientation, const TSet<EPDFFlags>& Flags);
```

### `RenderPage`
* Renders the page to a texture.
- param Start The start position to render the page.
- param Size The size of the rendered page in pixel.
- param Orientation The orientation of the page.
- param Flags Optional flags for the rendering.
- return A texture object containing the render of the page.
```cpp
void RenderPage(FPDFVector2D Start, FPDFVector2D Size, FLinearColor BackgroundColor, EPDFPageOrientation Orientation, TSet<EPDFFlags> Flags, FRenderPDFPageCallback Callback);
void RenderPage(FPDFVector2D Start, FPDFVector2D Size, EPDFPageOrientation Orientation, TSet<EPDFFlags> Flags, FRenderPDFPageCallback Callback);
void RenderPage(FPDFVector2D Start, FPDFVector2D Size, EPDFPageOrientation Orientation, FRenderPDFPageCallback Callback);
void RenderPage(FPDFVector2D Start, FPDFVector2D Size, FRenderPDFPageCallback Callback);
```

### `LoadImagesAsTexture`
- Loads all images in the page as texture.
- param Document Optional document. If specified, applies filter on the image as in the document. Otherwise, returns the raw image.
- return The images in the apge.

```cpp
TArray<UTexture2D*> LoadImagesAsTexture(class UPDFDocument* Document = nullptr);
```