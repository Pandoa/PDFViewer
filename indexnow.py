import requests
import xml.etree.ElementTree as ET

# -----------------------------
# CONFIG
# -----------------------------
KEY = "a90d2232de4c468fa8bdb63b980b6d79"
KEY_LOCATION = "https://pandoa.github.io/PDFViewer/a90d2232de4c468fa8bdb63b980b6d79.txt"
SITEMAP_URL = "https://pandoa.github.io/PDFViewer/sitemap.xml"

INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

# -----------------------------
# FETCH & PARSE SITEMAP
# -----------------------------
def get_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    urls = []
    for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        urls.append(url.text.strip())

    return urls

# -----------------------------
# BUILD INDEXNOW PAYLOAD
# -----------------------------
def send_indexnow(url_list):
    payload = {
        "host": "pandoa.github.io",
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": url_list
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.post(INDEXNOW_ENDPOINT, json=payload, headers=headers, timeout=30)

    print("Status code:", response.status_code)
    print("Response:", response.text)


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    urls = get_urls_from_sitemap(SITEMAP_URL)

    # optional: filter only your PDFViewer URLs (already likely all are)
    urls = [u for u in urls if "pandoa.github.io/PDFViewer" in u]

    send_indexnow(urls)