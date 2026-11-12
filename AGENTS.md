# AGENTS.md

Hinweise für KI-Agenten, die in diesem Repository arbeiten. Gilt für alle
Sessions und Werkzeuge (OpenCode, Claude Code, …). Wenn etwas hier nicht
geregelt ist: nachfragen, nicht raten.

## Was das ist

Private Website und Blog von Simon Dückert: **MkDocs Material** mit dem
`blog`-Plugin, `docs_dir: src`, veröffentlicht auf <https://dueckert.eu> über
GitHub Pages. Der Build läuft in `.github/workflows/generate-website.yml`.

## Bauen und prüfen

```bash
uv run --with-requirements requirements.txt mkdocs build
uv run --with-requirements requirements.txt mkdocs serve   # Vorschau auf :8000
```

Immer exakt diese Befehle verwenden – sie nutzen die in `requirements.txt`
gepinnten Versionen. Der Build gibt bekannte Warnungen aus (Altbeiträge mit
falschen Bildpfaden, `feed_rss_created.xml`); das sind **keine** neuen Fehler.
Ein Build gilt als erfolgreich, wenn er mit Exit-Code 0 endet.

## Neuen Beitrag anlegen

1. Branch `blog/<slug>` von `main`.
2. Datei `src/posts/<Jahr>/<slug>.md` (Jahr = Erscheinungsjahr, kebab-case).
3. Frontmatter und Aufbau wie unten.
4. Bilder nach `src/posts/images/` legen.
5. `draft: false` setzen, wenn der Beitrag erscheinen soll.
6. Build laufen lassen, dann committen, pushen, PR öffnen.

## Frontmatter

```yaml
---
date: 2026-11-12          # Pflicht, bestimmt die URL
slug: panang-curry        # Pflicht, pinnt die URL
categories:               # Pflicht
  - Rezepte
tags:                     # Pflicht
  - thailand
  - curry
draft: true               # Pflicht: true = Entwurf, false = veröffentlichen
---
```

- **Kein `title:` im Frontmatter.** Der Titel steht als `# Überschrift` in der
  ersten Zeile nach dem Frontmatter – so machen es alle neueren Beiträge.
- `slug` und `date` eines **veröffentlichten** Beitrags niemals ändern: beide
  stehen in der URL. Korrekturen am Titel sind dagegen unkritisch, weil der
  Slug die URL pinnt.

## Aufbau eines Beitrags

```markdown
# Titel

Zwei bis drei Sätze Einleitung. Sie erscheinen in der Übersicht, im RSS-Feed
und in llms.txt.

<!-- more -->

![](../images/beispiel.png)

## Abschnitt

Text
```

- Rezepte: `## Zutaten (n Portionen)` als Liste, `## Zubereitung` als
  nummerierte Schritte, optional `## Weblinks`.
- Alt-Text auf Bildern auf Englisch (wie in den bestehenden Beiträgen).

## Bilder

- Ablage: `src/posts/images/<sprechender-name>.png`
- Einbindung relativ: `../images/<name>.png` (Obsidian erzeugt das automatisch)
- Format 16:9, z. B. 1280×720 oder 960×576
- Keine fremden Bilder einbinden. Fehlt ein Bild: `TODO` setzen und fragen.

## Kategorien und Tags

Bestehende Kategorien verwenden, keine neuen erfinden (aktuell u. a.
`Rezepte`, `Digitalität`, `Reisen`, `lernOS`, `Cogneon`, `Persönliches`).
Tags klein schreiben, keine Leerzeichen. Im Zweifel nachfragen.

## URLs

Schema: `/<Jahr>/<Monat>/<Tag>/<slug>/`. Die URL entsteht aus `date` und
`slug`, **nicht** aus dem Dateinamen. Dateien dürfen umbenannt werden, ohne
dass Links brechen – `slug` und `date` nicht.

## Pull Requests

- Ein PR pro Beitrag, Branch `blog/<slug>`; Infrastruktur-Änderungen unter
  `chore/<thema>`.
- Commits und PR-Titel auf Deutsch, kurz, ohne Präfix und ohne Emoji
  (z. B. `Rezept Panang Curry`), **keine** Agenten-Co-Autoren-Zeile.
- PR-Beschreibung nach `.github/PULL_REQUEST_TEMPLATE.md` ausfüllen.
- `main` ist geschützt: Merge nur über PR mit grünem `build`-Check.
- Squash-Merge, Branch danach löschen.

## llms.txt

`llms.txt` wird bei jedem Build von `hooks/llms_txt.py` erzeugt. **Nicht von
Hand anlegen oder bearbeiten** – Änderungen gehören in den Hook oder in die
Beiträge.

## Nicht anfassen

Ohne ausdrücklichen Auftrag **nicht** ändern:

- bestehende Beiträge (Rechtschreibung, Bildpfade, Formatierung),
- Theme, `src/overrides/`, `src/stylesheets/`,
- Plugin-Versionen in `requirements.txt`,
- Struktur von `mkdocs.yml` (nav, Plugins, Theme-Optionen),
- `src/CNAME` und die Domain-Konfiguration.

Aufräumarbeiten an Altinhalten sind eigene, ausdrücklich beauftragte PRs.

## Inhaltliche Regeln

- **Keine erfundenen Fakten.** Unklare Angaben als `TODO` markieren, nicht
  plausibel formulieren.
- Deutsch, Ich-Form, Ton wie in den bestehenden Beiträgen.
- Quellen verlinken; fremde Texte nicht übernehmen, nur Fakten (z. B. Zutaten
  und Mengen) und dafür eigene Formulierungen verwenden.
