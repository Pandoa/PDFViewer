# `UPDFDocument`

## Functions

### `LoadDocumentSync`
- Loads a PDF document from disk synchronously.
- param Path The path of the PDF document. Must be accessible through the stadard filesystem.
- param Password The optional password of the PDF document.
- return A new Document object.
```cpp
static UPDFDocument* LoadDocumentSync(const FString& Path, const FString& Password, FString& OutError, int32& OutErrorCode);
static UPDFDocument* LoadDocumentSync(const FString& Path, const FString& Password);
```

### `LoadDocument`
- Loads a PDF document from disk asynchronously.
- param Path The path of the PDF document. Must be accessible through the stadard filesystem.
- param Password The optional password of the PDF document.
- param Callback The callback called when the document is loaded.
```cpp
static void LoadDocument(FString Path, FString Password, FLoadPDFDocumentCallback Callback);
```

### `LoadDocumentFromMemorySync`
- Loads a PDF document from memory synchronously.
- param Data The data of the document.
- param Password The optional password of the PDF document.
- return A new Document object.

```cpp
static UPDFDocument* LoadDocumentFromMemorySync(const TArray<uint8>& Data, const FString& Password, FString& OutError, int32& OutErrorCode);
```

### `LoadDocumentFromMemory`
- Loads a PDF document from disk asynchronously.
- param Data The data of the PDF document. 
- param Password The optional password of the PDF document.
- param Callback The callback called when the document is loaded.

```cpp
static void LoadDocumentFromMemory(TArray<uint8> Data, FString Password, FLoadPDFDocumentCallback Callback);
static void LoadDocumentFromMemory(TSharedPtr<TArray<uint8>> Data, FString Password, FLoadPDFDocumentCallback Callback);
```

### `LoadPagesAsTextureSync`
- Loads a PDF file as a list of textures representing each page in order synchronously.
- param Path The path of the document.
- param Password The password of the document.
- return A texture for each page inside of the PDF file.

```cpp
static TArray<UTexture2D*> LoadPagesAsTextureSync(const FString& Path, const FString& Password, const FPDFPageParameters& PageParams, FString& OutError, int32& OutErrorCode);
static TArray<UTexture2D*> LoadPagesAsTextureSync(const FString& Path, const FString& Password, const FPDFPageParameters& PageParams);
```

### `LoadPagesAsTexture`
- Loads a PDF file as a list of textures representing each page in order synchronously.
- param Path The path of the document.
- param Password The password of the document.
- return A texture for each page inside of the PDF file.

```cpp
static void LoadPagesAsTexture(FString Path, FString Password, FPDFPageParameters PageParams, FLoadPDFPagesCallback Callback);
```

### `GetPage`
- Gets the page at the specified index.
- param Index The index of the page we want.
- return The page at the specified index or nullptr if there are none.

```cpp
class UPDFPage* GetPage(const int32 Index);
```

### `GetPageCount`
- Gets the number of pages in the document.
- return The number of pages in the document.

```cpp
int32 GetPageCount() const;
```

### `LoadImagesAsTexture`
- Loads all images in the document as textures.
- return All the images in the document.

```cpp
TArray<UTexture2D*> LoadImagesAsTexture();
```


