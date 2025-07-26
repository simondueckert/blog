---
title: "Kim Jong-Muskifizierung von Twitter"
date: 2022-12-17
categories: 
  - "fediverse"
  - "mastodon"
  - "musk"
  - "twitter"
---

![](./images/kimjongmusk-2.jpeg)

Da **Elon Musk** sich nach der Übernahme von **Twitter** wie ein **verrückter Diktator** aufspielt, habe ich mein Konto dort eingefroren und bin [nach Mastodon umgezogen](https://chaos.social/@sdueckert). Um möglichst vielen Menschen [Mastodon](https://de.wikipedia.org/wiki/Mastodon_\(Software\)) zu erklären, habe ich [diese kleine Webpräsentation](https://simondueckert.github.io/presentations/mastodon-intro/index.html) erstellt, die ihr gerne in Euren Kontexten verwenden könnt.

<!-- more -->

Außerdem habe ich mir mein Twitter-Archiv heruntergeladen. Twitter stellt das als ZIP-Datei mit gepackten JSON-Dateien zur Verfügung. Ich habe überlegt, wie ich das in Zukunft selber einfach nutzen und gleichzeitig öffentlich bereitstellen kann. Herausgekommen ist [die Website Tweetbook auf Github](https://simondueckert.github.io/tweetbook/) mit einem monatsweisen Archiv und einer Volltextsuche. In diesem Blog erkläre ich kurz, in welchen Schritten Ihr euch auch so eine Website erstellen könnt.

## Schritt-für-Schritt-Anleitung

1. Fordere auf Twitter das Archiv Deiner Daten an ([Anleitung](https://help.twitter.com/de/managing-your-account/how-to-download-your-twitter-archive), kann 1-2 Tage dauern).

3. Installiere Python auf deinem Computer (wenn Du es noch nicht hast) ([Download](https://www.python.org/downloads/)).

5. Lade Dir das Python-Skript parser.py von Tim Hutton herunter und führe es aus ([Anleitung](https://github.com/timhutton/twitter-archive-parser)).

7. Installiere den Static Site Generator [MkDocs](https://www.mkdocs.org/).

9. Installiere [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

11. Erstelle eine Datei mkdocs.yml zur Konfiguration von MkDocs ([Beispiel meiner mkdocs.yml](https://github.com/simondueckert/tweetbook/blob/main/mkdocs.yml)).

13. Generiere die Website mit dem Befehl _mkdocs build_.

15. Lade die generierten Dateien in einen Webspace hoch (ich verwende wie bei [lernOS](https://lernos.org) Github Pages, es geht aber aber auch jeder andere Webspace).

So sieht das Ergebnis dann aus:

![Screenshot der Website Tweetbook von Simon Dückert](images/Bildschirm­foto-2022-12-17-um-12.26.09-1024x620.png)
