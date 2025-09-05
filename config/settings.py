import os

HOME_DIR = os.path.expanduser("~")
DEFAULT_DOWNLOAD_PATH = os.path.join(HOME_DIR, "YT_Downloads")

os.makedirs(DEFAULT_DOWNLOAD_PATH, exist_ok=True)
