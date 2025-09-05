# 🎬 YouTube Downloader  

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-1.38+-brightgreen.svg)](https://streamlit.io/)  
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-orange.svg)](https://github.com/yt-dlp/yt-dlp)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

**YouTube Downloader** is a clean and minimal **web app** built with **Streamlit** and **yt-dlp**. It allows users to download YouTube videos and Shorts in multiple resolutions and save them directly to any folder on their device without manually typing paths. The app features a dark-themed, responsive UI and automatically organizes downloads into subfolders. It works seamlessly across macOS, Windows, and Linux.  

---

## ✨ Features  
- ✅ Download regular YouTube videos and Shorts  
- ✅ Select from multiple available resolutions  
- ✅ Choose any folder on your device as the save location  
- ✅ Auto-creates subfolders for better organization  
- ✅ Minimal, dark-themed, responsive UI  
- ✅ Cross-platform (macOS, Windows, Linux)  

---

## 📂 Project Structure  

```bash
YT Vid Downloader/
├── backend/
│   ├── __init__.py
│   ├── downloader.py     # Core logic for fetching & downloading videos
│   ├── utils.py          # Utility functions (paths, validation, etc.)
├── config/
│   ├── __init__.py
│   ├── settings.py       # Configurable defaults (download path, etc.)
├── app.py                # Streamlit frontend
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/YT-Vid-Downloader.git
cd YT-Vid-Downloader
```
## Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
## Install dependencies and run the webapp

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📄 License
This project is licensed under the MIT License.

