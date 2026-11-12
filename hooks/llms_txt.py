"""Erzeugt beim Build eine llms.txt (https://llmstxt.org/) im Site-Root.

Die Datei wird aus den Beitraegen generiert und bleibt damit automatisch
aktuell: keine zweite Liste, die gepflegt werden muss.

Grundsatz: Dieser Hook darf den Build niemals abbrechen. Wenn ein Beitrag
nicht lesbar ist, wird er uebersprungen und das Problem geloggt.
"""

from __future__ import annotations

import logging
import re
from html import unescape
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.llms_txt")

# Einstiegspunkte der Website. Entspricht der nav in mkdocs.yml.
PAGES = [
    ("Startseite", "", "Einstieg und neueste Beiträge"),
    ("Über mich", "about/", "Wer schreibt hier"),
    ("Projekte", "projects/", "Projekte und Vorhaben"),
    ("Publikationen", "publications/", "Veröffentlichungen"),
    ("Microblog", "microblog/", "Kurze Notizen"),
    ("Tags", "tags/", "Alle Beiträge nach Schlagworten"),
]

MAX_DESCRIPTION = 200

# src_uri -> {description, title, url, sort}
_posts: dict[str, dict] = {}

_MD_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
_HTML_TAG = re.compile(r"<[^>]+>")
_WHITESPACE = re.compile(r"\s+")
_DATE_IN_URL = re.compile(r"^(\d{4})/(\d{2})/(\d{2})/")
_LIST_OR_HEADING = re.compile(r"^(\d+\.|[-*+]\s|#{1,6}\s|!|<!--|---|\||<)")


def _plain(text: str) -> str:
    """Markdown/HTML grob zu reinem Text reduzieren."""
    text = _MD_LINK.sub(r"\1", text)
    text = _HTML_TAG.sub(" ", text)
    text = unescape(text)
    for char in "*_`>#":
        text = text.replace(char, " ")
    return _WHITESPACE.sub(" ", text).strip()


def _first_paragraph(markdown: str) -> str:
    """Ersten echten Absatz eines Beitrags als Kurzbeschreibung ziehen."""
    for block in re.split(r"\n\s*\n", markdown):
        block = block.strip()
        if not block or _LIST_OR_HEADING.match(block):
            continue
        text = _plain(block)
        if not text:
            continue
        if len(text) > MAX_DESCRIPTION:
            text = text[:MAX_DESCRIPTION].rsplit(" ", 1)[0] + " …"
        return text
    return ""


def _absolute(config, url: str) -> str:
    base = (config.site_url or "/").rstrip("/") + "/"
    return base + (url or "").lstrip("/")


def on_pre_build(*, config):
    # Bei `mkdocs serve` laeuft der Build mehrfach im selben Prozess.
    _posts.clear()


def on_page_markdown(markdown, *, page, config, files):
    try:
        if not page.file.src_uri.startswith("posts/"):
            return
        _posts[page.file.src_uri] = {"description": _first_paragraph(markdown)}
    except Exception:  # noqa: BLE001 - Build nie abbrechen
        log.debug("llms.txt: Beschreibung nicht ermittelbar", exc_info=True)


def on_page_context(context, *, page, config, nav):
    try:
        entry = _posts.get(page.file.src_uri)
        if entry is None or page.meta.get("draft"):
            return
        match = _DATE_IN_URL.match(page.url or "")
        if not match:
            return
        year, month, day = (int(part) for part in match.groups())
        entry.update(
            title=page.title or page.file.name,
            url=_absolute(config, page.url),
            sort=(year, month, day, page.url or ""),
        )
    except Exception:  # noqa: BLE001 - Build nie abbrechen
        log.debug("llms.txt: Metadaten nicht ermittelbar", exc_info=True)


def on_post_build(*, config):
    try:
        posts = sorted(
            (post for post in _posts.values() if post.get("url")),
            key=lambda post: post["sort"],
            reverse=True,
        )

        lines = [
            f"# {config.site_name}",
            "",
            f"> {config.site_description or config.site_name}",
            "",
            "## Seiten",
            "",
        ]
        for title, path, description in PAGES:
            lines.append(f"- [{title}]({_absolute(config, path)}): {description}")

        lines += ["", "## Beiträge", ""]
        current_year = None
        for post in posts:
            year = post["sort"][0]
            if year != current_year:
                if current_year is not None:
                    lines.append("")
                current_year = year
                lines += [f"### {year}", ""]
            description = post.get("description") or ""
            suffix = f": {description}" if description else ""
            lines.append(f"- [{post['title']}]({post['url']}){suffix}")

        lines += [
            "",
            "## Feeds",
            "",
            f"- [RSS-Feed]({_absolute(config, 'feed_rss_created.xml')}): neue Beiträge abonnieren",
            "",
        ]

        target = Path(config.site_dir) / "llms.txt"
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
        log.info("llms.txt geschrieben: %d Beiträge", len(posts))
    except Exception:  # noqa: BLE001 - Build nie abbrechen
        log.warning("llms.txt konnte nicht geschrieben werden", exc_info=True)
