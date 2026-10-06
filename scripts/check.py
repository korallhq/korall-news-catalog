"""Check catalog.yml and optionally write catalog.opml.

    python scripts/check.py                     # format and rules
    python scripts/check.py --base old.yml      # also: version raised, new feeds reachable
    python scripts/check.py --opml catalog.opml # also: write the OPML export

Rules mirror what korall accepts: only public feed addresses, unique URLs, dates not after
the catalogue version. korall drops anything else, so the check catches it before merging.
"""

from __future__ import annotations

import argparse
import gzip
import ipaddress
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path
from urllib.parse import urlsplit

import yaml

DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
LOCAL_SUFFIXES = (".local", ".lan", ".home", ".internal", ".localhost", ".arpa", ".intranet", ".corp")
FEED_TAGS = ("<rss", "<feed", "<rdf:RDF", "<rdf")


def public_url(url: str) -> bool:
    parts = urlsplit(url)
    host = (parts.hostname or "").rstrip(".").lower()
    if parts.scheme not in {"http", "https"} or not host or parts.username or parts.password:
        return False
    try:
        return ipaddress.ip_address(host).is_global
    except ValueError:
        return "." in host and not host.endswith(LOCAL_SUFFIXES)


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def problems(data: dict) -> list[str]:
    found = []
    version = str(data.get("version") or "")
    if not DATE.fullmatch(version):
        found.append("version must be a date (YYYY-MM-DD)")
    seen: dict[str, str] = {}
    folders = data.get("folders")
    if not isinstance(folders, list) or not folders:
        return found + ["folders must be a non-empty list"]
    for folder in folders:
        name = str((folder or {}).get("title") or "")
        if not name:
            found.append("every folder needs a title")
        for item in (folder or {}).get("sources") or []:
            url = str(item.get("url") or "").strip()
            label = f"{name} / {item.get('title') or url}"
            if not item.get("title"):
                found.append(f"{label}: title missing")
            if not public_url(url):
                found.append(f"{label}: url must be a public http(s) address")
            if url.rstrip("/") in seen:
                found.append(f"{label}: url also listed under {seen[url.rstrip('/')]}")
            seen[url.rstrip("/")] = label
            added = str(item.get("added") or "")
            if added and (not DATE.fullmatch(added) or added > version):
                found.append(f"{label}: added must be a date not after the version")
            replaces = item.get("replaces") or []
            for old in [replaces] if isinstance(replaces, str) else replaces:
                if not public_url(str(old)):
                    found.append(f"{label}: replaces must be a public http(s) address")
    for item in data.get("removed") or []:
        url = str(item.get("url") or "").strip()
        day = str(item.get("removed") or "")
        if not url or not DATE.fullmatch(day) or day > version:
            found.append(f"removed {url or '?'}: needs url and a removed date not after the version")
        if url.rstrip("/") in seen:
            found.append(f"removed {url}: still listed as a source")
    return found


def urls(data: dict) -> set[str]:
    return {str(item["url"]).strip() for folder in data["folders"] for item in folder.get("sources") or []}


def reachable(url: str) -> str:
    """Empty when the address answers with a feed, otherwise the reason."""
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; korall-news-catalog check)"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = response.read(262144)
    except OSError as exc:
        return str(exc)
    if data[:2] == b"\x1f\x8b":  # some servers compress without being asked
        try:
            data = gzip.decompress(data)
        except (OSError, EOFError):
            data = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(data)
    head = data[:4096].decode("utf-8", errors="replace")
    return "" if any(tag in head for tag in FEED_TAGS) else "no RSS or Atom feed"


def opml(data: dict) -> str:
    root = ET.Element("opml", version="2.0")
    ET.SubElement(ET.SubElement(root, "head"), "title").text = f"korall news catalog {data['version']}"
    body = ET.SubElement(root, "body")
    for folder in data["folders"]:
        outline = ET.SubElement(body, "outline", text=folder["title"], title=folder["title"])
        for item in folder.get("sources") or []:
            attributes = {"type": "rss", "text": item["title"], "title": item["title"], "xmlUrl": item["url"]}
            if item.get("website"):
                attributes["htmlUrl"] = item["website"]
            ET.SubElement(outline, "outline", **attributes)
    ET.indent(root)
    return ET.tostring(root, encoding="unicode", xml_declaration=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", nargs="?", default="catalog.yml", type=Path)
    parser.add_argument("--base", type=Path, help="catalogue before the change")
    parser.add_argument("--opml", type=Path, help="write the OPML export here")
    args = parser.parse_args()
    data = load(args.catalog)
    found = problems(data)
    if args.base and not found:
        base = load(args.base)
        if args.catalog.read_text(encoding="utf-8") != args.base.read_text(encoding="utf-8") and \
                str(data["version"]) <= str(base.get("version") or ""):
            found.append(f"catalogue changed: raise version above {base.get('version')}")
        for url in sorted(urls(data) - urls(base)):
            reason = reachable(url)
            if reason:
                found.append(f"{url}: {reason}")
    for problem in found:
        print(f"::error file={args.catalog}::{problem}")
    if found:
        return 1
    if args.opml:
        args.opml.write_text(opml(data), encoding="utf-8")
    print(f"catalog {data['version']}: {len(urls(data))} sources in {len(data['folders'])} folders")
    return 0


if __name__ == "__main__":
    sys.exit(main())
