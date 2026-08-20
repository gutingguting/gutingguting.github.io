#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PODCAST_DIR = ROOT / "public" / "podcast"
EPISODES_JSON = PODCAST_DIR / "episodes.json"
FEED_XML = PODCAST_DIR / "feed.xml"
COVER_PNG = PODCAST_DIR / "cover.png"
WORK_DIR = ROOT / "work"

ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
ET.register_namespace("itunes", ITUNES_NS)
ET.register_namespace("content", CONTENT_NS)


def run(cmd: list[str], capture: bool = False) -> str:
    print("+", " ".join(cmd), flush=True)
    proc = subprocess.run(
        cmd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
    )
    return proc.stdout if capture else ""


def safe_ascii_id(extractor: str, raw_id: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]", "", f"{extractor}{raw_id}")
    if not value:
        raise RuntimeError("Could not derive an ASCII-safe episode id.")
    return value[:120]


def load_episodes() -> list[dict]:
    if not EPISODES_JSON.exists():
        return []
    return json.loads(EPISODES_JSON.read_text(encoding="utf-8"))


def save_episodes(episodes: list[dict]) -> None:
    PODCAST_DIR.mkdir(parents=True, exist_ok=True)
    EPISODES_JSON.write_text(
        json.dumps(episodes, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def ensure_cover() -> None:
    if COVER_PNG.exists():
        return
    from PIL import Image, ImageDraw, ImageFont

    size = 1400
    image = Image.new("RGB", (size, size), (246, 246, 246))
    draw = ImageDraw.Draw(image)
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]

    def font(px: int):
        for fp in font_paths:
            if Path(fp).exists():
                return ImageFont.truetype(fp, px)
        return ImageFont.load_default()

    draw.rectangle((90, 90, size - 90, size - 90), outline=(25, 25, 25), width=12)
    draw.text((140, 430), "LATERCAST", font=font(150), fill=(20, 20, 20))
    draw.text((145, 640), "MY WATCH LATER", font=font(62), fill=(70, 70, 70))
    draw.text((145, 1000), "VIDEO -> PODCAST", font=font(42), fill=(110, 110, 110))
    COVER_PNG.parent.mkdir(parents=True, exist_ok=True)
    image.save(COVER_PNG, "PNG", optimize=True)


def xml_clean(value: object) -> str:
    text = str(value if value is not None else "")
    return "".join(ch for ch in text if ch in "\t\n\r" or ord(ch) >= 0x20)


def duration_text(seconds: int | float | None) -> str:
    total = int(round(float(seconds or 0)))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def is_bilibili(url: str) -> bool:
    value = url.lower()
    return "bilibili.com/" in value or "b23.tv/" in value


def ytdlp_prefix(url: str) -> list[str]:
    # For Bilibili we run the patched upstream extractor together with a real
    # browser TLS fingerprint. The extractor itself manages buvid/buvid_fp and
    # Bilibili's current 412/v_voucher handling.
    if is_bilibili(url):
        return ["yt-dlp", "--impersonate", "chrome"]
    return ["yt-dlp"]


def write_index(site_url: str) -> None:
    feed_url = f"{site_url.rstrip('/')}/podcast/feed.xml"
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LaterCast</title></head>
<body><main><h1>LaterCast</h1><p>我的稍后听 Podcast。</p><p>RSS: <a href="{feed_url}">{feed_url}</a></p></main></body>
</html>
"""
    (PODCAST_DIR / "index.html").write_text(html, encoding="utf-8")


def build_feed(episodes: list[dict], site_url: str, home_url: str) -> None:
    site_url = site_url.rstrip("/")
    rss = ET.Element("rss", {"version": "2.0", "xmlns:content": CONTENT_NS})
    channel = ET.SubElement(rss, "channel")

    def child(parent, tag, text=None, attrib=None):
        el = ET.SubElement(parent, tag, attrib or {})
        if text is not None:
            el.text = xml_clean(text)
        return el

    child(channel, "title", "我的稍后听 · LaterCast")
    child(channel, "link", home_url)
    child(channel, "description", "把长视频变成适合在 Apple Podcasts 里收听的个人稍后听列表。")
    child(channel, "language", "zh-cn")
    child(channel, "lastBuildDate", format_datetime(datetime.now(timezone.utc), usegmt=True))
    child(channel, f"{{{ITUNES_NS}}}author", "LaterCast")
    child(channel, f"{{{ITUNES_NS}}}summary", "Personal watch-later audio feed.")
    child(channel, f"{{{ITUNES_NS}}}explicit", "false")
    child(channel, f"{{{ITUNES_NS}}}type", "episodic")
    child(channel, f"{{{ITUNES_NS}}}block", "true")
    ET.SubElement(channel, f"{{{ITUNES_NS}}}image", {"href": f"{site_url}/podcast/cover.png"})

    image = child(channel, "image")
    child(image, "url", f"{site_url}/podcast/cover.png")
    child(image, "title", "我的稍后听 · LaterCast")
    child(image, "link", home_url)

    for ep in sorted(episodes, key=lambda x: x["added_at"], reverse=True):
        item = child(channel, "item")
        child(item, "title", ep["title"])
        child(item, "link", ep["source_url"])
        description = f"来源：{ep.get('uploader') or ep.get('extractor') or 'video'}"
        if ep.get("description"):
            description += "\n\n" + ep["description"][:1200]
        child(item, "description", description)
        dt = datetime.fromisoformat(ep["added_at"].replace("Z", "+00:00")).astimezone(timezone.utc)
        child(item, "pubDate", format_datetime(dt, usegmt=True))
        child(item, "guid", ep["guid"], {"isPermaLink": "false"})
        ET.SubElement(item, "enclosure", {
            "url": ep["audio_url"],
            "length": str(ep["length"]),
            "type": "audio/mp4",
        })
        child(item, f"{{{ITUNES_NS}}}duration", duration_text(ep.get("duration")))
        child(item, f"{{{ITUNES_NS}}}episodeType", "full")
        child(item, f"{{{ITUNES_NS}}}explicit", "false")

    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ")
    FEED_XML.parent.mkdir(parents=True, exist_ok=True)
    tree.write(FEED_XML, encoding="utf-8", xml_declaration=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a LaterCast episode from a video URL.")
    parser.add_argument("url")
    args = parser.parse_args()

    repo = os.environ.get("GITHUB_REPOSITORY", "gutingguting/gutingguting.github.io")
    branch = os.environ.get("LATERCAST_BRANCH", "latercast")
    default_site_url = f"https://raw.githubusercontent.com/{repo}/{branch}/public"
    site_url = os.environ.get("LATERCAST_SITE_URL", default_site_url)
    home_url = os.environ.get("LATERCAST_HOME_URL", f"https://github.com/{repo}/tree/{branch}")

    PODCAST_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    ydl = ytdlp_prefix(args.url)
    meta_text = run(
        ydl + ["--dump-single-json", "--no-playlist", "--skip-download", args.url],
        capture=True,
    )
    meta = json.loads(meta_text)
    raw_id = str(meta.get("id") or "")
    extractor = str(meta.get("extractor_key") or meta.get("extractor") or "video")
    safe_id = safe_ascii_id(extractor, raw_id)
    tag = f"ep{safe_id}"
    asset_name = f"{safe_id}.m4a"
    audio_path = WORK_DIR / asset_name

    for old in WORK_DIR.glob("source.*"):
        old.unlink()

    run(
        ydl + [
            "--no-playlist",
            "-f", "bestaudio/best",
            "-o", str(WORK_DIR / "source.%(ext)s"),
            args.url,
        ]
    )

    sources = [p for p in WORK_DIR.glob("source.*") if p.is_file()]
    if not sources:
        raise RuntimeError("yt-dlp finished but no source audio file was found.")
    source = max(sources, key=lambda p: p.stat().st_size)

    run([
        "ffmpeg", "-y", "-i", str(source), "-vn",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
        "-movflags", "+faststart", str(audio_path),
    ])

    ffprobe_out = run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path),
    ], capture=True).strip()
    duration = int(round(float(ffprobe_out))) if ffprobe_out else int(meta.get("duration") or 0)

    audio_url = f"https://github.com/{repo}/releases/download/{tag}/{asset_name}"
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    episodes = load_episodes()
    existing = next((ep for ep in episodes if ep.get("guid") == safe_id), None)
    added_at = existing.get("added_at") if existing else now

    episode = {
        "guid": safe_id,
        "source_id": raw_id,
        "extractor": extractor,
        "title": str(meta.get("title") or raw_id or "Untitled"),
        "uploader": str(meta.get("uploader") or meta.get("channel") or ""),
        "source_url": str(meta.get("webpage_url") or args.url),
        "description": str(meta.get("description") or ""),
        "duration": duration,
        "length": audio_path.stat().st_size,
        "added_at": added_at,
        "audio_url": audio_url,
        "tag": tag,
        "asset_name": asset_name,
    }

    episodes = [ep for ep in episodes if ep.get("guid") != safe_id]
    episodes.append(episode)
    save_episodes(episodes)
    ensure_cover()
    write_index(site_url)
    build_feed(episodes, site_url, home_url)

    result = {
        "guid": safe_id,
        "title": episode["title"],
        "tag": tag,
        "asset_path": str(audio_path),
        "asset_name": asset_name,
        "audio_url": audio_url,
        "feed_url": f"{site_url.rstrip('/')}/podcast/feed.xml",
    }
    (WORK_DIR / "latercast-result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
