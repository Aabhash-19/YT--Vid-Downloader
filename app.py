import os
import streamlit as st

from backend import fetch_streams, download_stream, validate_url, get_download_path
from config import DEFAULT_DOWNLOAD_PATH

st.set_page_config(page_title="YouTube Downloader", page_icon="🎥", layout="centered")
st.title("🎥 YouTube Downloader")
st.caption("Download regular YouTube videos and Shorts with selectable quality.")


url = st.text_input("Paste YouTube URL (video or Shorts):", placeholder="https://www.youtube.com/watch?v=...")

import os

def list_dirs(base_path):

    try:
        return [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    except Exception:
        return []

home_dir = os.path.expanduser("~")
default_base = get_download_path() 

st.write("📂 Choose a save folder:")

base_path = st.text_input("Base path:", value=default_base)
dirs = list_dirs(base_path)

selected = st.selectbox("Subfolders:", ["(base)"] + dirs)

if selected == "(base)":
    save_path = base_path
else:
    save_path = os.path.join(base_path, selected)

st.caption(f"✅ Videos will be saved to: `{save_path}`")


col1, col2 = st.columns(2)
with col1:
    fetch_btn = st.button("Fetch Formats")
with col2:
    download_btn = st.button("Download")


if "formats" not in st.session_state:
    st.session_state.formats = []
if "video_title" not in st.session_state:
    st.session_state.video_title = ""
if "thumbnail" not in st.session_state:
    st.session_state.thumbnail = ""


if fetch_btn:
    st.session_state.formats = []
    st.session_state.video_title = ""
    st.session_state.thumbnail = ""

    if not url or not validate_url(url):
        st.error("Please enter a valid YouTube URL.")
    else:
        with st.spinner("Fetching available formats..."):
            try:
                info, formats = fetch_streams(url)
                st.session_state.video_title = info.get("title", "Untitled")
                st.session_state.thumbnail = info.get("thumbnail", "")
                st.session_state.formats = formats
            except Exception as e:
                st.error(f"Failed to fetch formats: {e}")

if st.session_state.video_title:
    st.subheader(st.session_state.video_title)
if st.session_state.thumbnail:
    st.image(st.session_state.thumbnail, width=420, caption="Thumbnail")

format_choice = None
if st.session_state.formats:
    options = [
        f"{f['label']}  ·  id={f['format_id']}  ·  ~{f['filesize_h']}"
        for f in st.session_state.formats
    ]
    format_choice = st.selectbox("Choose quality/format:", options)

if download_btn:
    if not url or not validate_url(url):
        st.error("Please enter a valid YouTube URL.")
    elif not st.session_state.formats:
        st.warning("Fetch formats first, then choose one to download.")
    elif not format_choice:
        st.warning("Please select a format.")
    else:

        try:
            os.makedirs(save_path, exist_ok=True)
        except Exception as e:
            st.error(f"Invalid save folder: {e}")
        else:

            try:
                format_id = format_choice.split("id=")[-1].split()[0]
            except Exception:
                st.error("Could not parse selected format. Please fetch again.")
                st.stop()

            with st.spinner("Downloading..."):
                try:
                    output_file = download_stream(url, format_id, save_path)
                    st.success("✅ Download complete!")
                    if output_file and os.path.exists(output_file):
                        st.write(f"Saved to: `{output_file}`")
                except Exception as e:
                    st.error(f"Download failed: {e}")
