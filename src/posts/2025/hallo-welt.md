---
title: "Hallo MkDocs Welt!"
date: 2025-06-22
categories:
  - infrastruktur
  - weblog
  - mkdocs
  - lernos
---

Ich habe ein kleines [Projekt](../../projects/2025-blog-migration.md) aufgesetzt, um mein [privates Blog](https://blog.dueckert.eu/) von Wordpress auf den statischen Seitengenerator [MkDocs](https://www.mkdocs.org/) umzusetzen, den wir auch im [lernOS Projekt](https://lernos.org) verwenden. Sobald die Inhalte alle umgezogen und getestet sind, schalte ich auch die Domain um. Die Links müssten robust sein, d.h. im neuen System sind (fast) alle Inhalte unter den gleichen URLs zu erreichen. Ich hoffe, dass durch die Vereinfachung, das bloggen wieder etwas mehr zur Routine wird.

Die Inhalte schreibe ich jetzt alle in Markdown (das geht auch bequem auf iPhone und iPad), verwalte sie mit Git(hub), erzeuge die Webseiten mit mkdocs und veröffentliche die Seiten auf Github Pages. Das Kommentarsystem ist mit Gisqus realisiert, dass alle Kommentare direkt in den Github-Diskussionen speichert:

```mermaid
flowchart LR
    A[Markdown] --> B(Mkdocs)
    B --> C(Github)
    C --> D(Github Pages)
```