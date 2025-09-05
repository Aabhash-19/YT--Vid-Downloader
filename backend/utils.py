import os

def validate_url(url: str) -> bool:
   
    if not isinstance(url, str):
        return False
    url = url.strip()
    return (
        url.startswith("https://www.youtube.com/") or
        url.startswith("http://www.youtube.com/") or
        url.startswith("https://youtu.be/") or
        url.startswith("http://youtu.be/")
    )

def get_download_path() -> str:
    """
    Return the default Downloads folder for the current user.
    """
    return os.path.join(os.path.expanduser("~"), "Downloads")
