from urllib.parse import urljoin, urlparse

def normalize_url(url, base_url):
    """Join relative URLs with base URL."""
    return urljoin(base_url, url)

def remove_duplicates(items):
    """Remove duplicates while keeping order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def is_valid_url(url):
    """Check if URL has valid scheme."""
    parsed = urlparse(url)
    return parsed.scheme in ["http", "https"]

