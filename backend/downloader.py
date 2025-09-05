import os
import yt_dlp

def _human_size(bytes_val):

    if bytes_val is None:
        return "unknown"
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(bytes_val)
    i = 0
    while size >= 1024 and i < len(units) - 1:
        size /= 1024.0
        i += 1
    return f"{size:.1f} {units[i]}"

def fetch_streams(url: str):
  
    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats_out = []
    for f in info.get("formats", []):

        if f.get("vcodec") == "none" or f.get("acodec") == "none":
            continue

        height = f.get("height")
        fps = f.get("fps")
        ext = f.get("ext")

        fs = f.get("filesize") or f.get("filesize_approx")

        label_parts = []
        if height: label_parts.append(f"{height}p")
        if ext: label_parts.append(f"{ext}")
        if fps: label_parts.append(f"{int(fps)}fps")
        label = " ".join(label_parts) if label_parts else f.get("format_note", "format")

        formats_out.append({
            "format_id": str(f.get("format_id")),
            "label": label,
            "filesize_h": _human_size(fs),
        })


    if not formats_out:
        best_id = info.get("format_id") or "best"
        formats_out.append({
            "format_id": str(best_id),
            "label": "best available",
            "filesize_h": "unknown",
        })


    basic_info = {
        "title": info.get("title"),
        "thumbnail": info.get("thumbnail"),
        "webpage_url": info.get("webpage_url"),
    }
    return basic_info, formats_out


def download_stream(url: str, format_id: str, save_path: str):
    
    os.makedirs(save_path, exist_ok=True)

    outtmpl = os.path.join(save_path, "%(title)s.%(ext)s")
    ydl_opts = {
        "format": format_id,
        "outtmpl": outtmpl,
        "merge_output_format": "mp4",   
        "quiet": False,
        "noprogress": True,
    }

    output_file = None

    def _hook(d):
        nonlocal output_file
        if d.get("status") == "finished":

            output_file = d.get("filename")

    ydl_opts["progress_hooks"] = [_hook]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_file
