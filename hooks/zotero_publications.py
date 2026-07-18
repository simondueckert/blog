"""MkDocs-Hook: bettet die oeffentliche Zotero-"My Publications"-Liste
zur Build-Zeit als Harvard-Literaturliste ein.

Auf der Publikationsseite wird der Marker <!-- ZOTERO_PUBLICATIONS -->
durch die von Zotero gerenderte Bibliographie ersetzt (CSL-Stil Harvard,
Locale de-DE, verlinkte URLs). Schlaegt der Abruf fehl (z.B. kein Netz),
bleibt eine Hinweismeldung stehen und der Build bricht NICHT ab.

Es wird 'format=json&include=bib' verwendet: Das liefert je Eintrag das
fertige, von Zotero gerenderte HTML und ist zuverlaessiger als das reine
'format=bib'. Der 'top'-Endpunkt schliesst Notizen/Anhaenge aus. Ein
API-Schluessel ist nicht noetig, da "My Publications" oeffentlich ist.
"""

import json
import os
import re
import urllib.error
import urllib.request

ZOTERO_USER_ID = "62674"
STYLE = "harvard-cite-them-right"
LOCALE = "de-DE"
MARKER = "<!-- ZOTERO_PUBLICATIONS -->"
PAGE_SIZE = 100

_ENTRY_RE = re.compile(r'<div class="csl-entry">.*?</div>', re.S)


def _api_url(start: int) -> str:
    return (
        f"https://api.zotero.org/users/{ZOTERO_USER_ID}/publications/items/top"
        f"?format=json&include=bib&style={STYLE}&locale={LOCALE}"
        f"&linkwrap=1&limit={PAGE_SIZE}&start={start}"
    )


def _fetch_items() -> list:
    # Offline-/Testmodus: JSON aus Datei statt Netzabruf
    sample = os.environ.get("ZOTERO_SAMPLE_FILE")
    if sample:
        with open(sample, encoding="utf-8") as fh:
            return json.load(fh)
    items: list = []
    start = 0
    while True:
        req = urllib.request.Request(
            _api_url(start),
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; blog.dueckert.eu build)",
                "Accept": "application/json",
                "Zotero-API-Version": "3",
            },
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            batch = json.loads(resp.read().decode("utf-8"))
        if not batch:
            break
        items.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        start += PAGE_SIZE
    return items


def _build_bibliography(items: list):
    # neueste zuerst
    items.sort(key=lambda it: it.get("meta", {}).get("parsedDate", ""), reverse=True)
    entries: list = []
    for item in items:
        entries.extend(_ENTRY_RE.findall(item.get("bib", "")))
    if not entries:
        return None
    inner = "\n".join(entries)
    return (
        '<div class="zotero-publications">\n'
        '<div class="csl-bib-body">\n'
        f"{inner}\n"
        "</div>\n</div>"
    )


def on_page_markdown(markdown, page=None, config=None, files=None, **kwargs):
    if MARKER not in markdown:
        return markdown
    try:
        block = _build_bibliography(_fetch_items())
        if block is None:
            block = (
                '!!! note "Keine Publikationen"\n'
                '    Aktuell sind keine Eintraege in "My Publications" vorhanden.'
            )
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", "replace")[:200]
        except Exception:
            pass
        block = (
            '!!! warning "Publikationsliste momentan nicht verfuegbar"\n'
            f"    Zotero antwortete mit HTTP {exc.code} ({exc.reason}). {detail}"
        )
    except Exception as exc:  # noqa: BLE001 - Build soll nicht scheitern
        block = (
            '!!! warning "Publikationsliste momentan nicht verfuegbar"\n'
            f"    Der Abruf ist fehlgeschlagen ({exc.__class__.__name__}: {exc}). "
            "Beim naechsten erfolgreichen Build erscheint die Liste wieder."
        )
    return markdown.replace(MARKER, block)
