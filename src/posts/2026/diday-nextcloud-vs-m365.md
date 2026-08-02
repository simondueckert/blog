---
date: 2026-08-02
categories:
    - Digitalität
tags:
    - Microsoft365
    - Nextcloud
    - diday
draft: false
---

# Nextcloud statt Micorosoft 365

Heute ist wieder [Digital Independence Day](https://di.day). Dieses Mal möchte ich darüber schreiben, wie man **statt Microsoft 365 **auch mit **Open Source Infrastruktur wie Nextcloud** arbeiten kann. Das geht im Privaten sogar noch einfacher, als geschäftlich. Bei [Cogneon](https://cogneon.de) habe ich letztes Jahr ein Projekt mit dem Namen **"Killswitch 365"** gestartet, mit dem Ziel, über Nacht von Microsoft 365 weggehen zu können und trotzdem arbeitsfähig zu bleiben.

<!-- more -->

Wir sind dort schon früh mit [Owncloud](https://owncloud.com/) gestartet und dann auf [Nextcloud](https://nextcloud.com/) gewechselt (beides selbst gehostet). Ursprünglich war der Hauptanwendungsfall, der Dateiserver hinter [unserem Mediawiki](https://wiki.cogneon.de) zu sein. Doch die Anwendungsfälle haben sich im Lauf der Zeit erweitert (z.B. Download-Bereich für Kunden, elektronische Bibliothek) und Nextcloud wurde Teil unserer "geschäftskritischen Infrastruktur" und wir haben das **Hosting an Hetzner ausgelagert** (Produkt: [StorageShare](https://www.hetzner.com/de/storage/storage-share/), nutze ich privat auch).

Im Rahmen des Killswitch-Projekts achte ich darauf, dass wir keine M365-Dienste verwenden, die man schwer ersetzen kann (keine Alternative, schwierige Datenmigraton etc.). Dazu gehören z.B. Microsoft Loop. Aus diesen Erfahrungen ist eine kleine Tabelle der **Nextcloud-Ersatzdienste** geworden, die ich hier gerne mit Euch teilen möchte:

| Kategorie                | M365-Dienst   | Nextcloud-Ersatz                                             | Bemerkung                                                                                                                                                                                 |
| ------------------------ | ------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dateien**              | Onedrive      | [Dateien](https://nextcloud.com/files/)                      | Das ist die Kernfunktion von Nextcloud, Desktop- und mobile Apps funktionieren sehr gut.                                                                                                  |
| **Dateien, Websites**    | Sharepoint    | [Team Folders](https://apps.nextcloud.com/apps/groupfolders) | Ordner, die mit einer Berechtigungsgruppe geteilt werden.                                                                                                                                 |
| **E-Mail**               | Outlook       | [Mail](https://apps.nextcloud.com/apps/cristal)              | Nextcloud hat keinen Mailserver, man braucht ein separates Postfach (ich nutze da privat auch Hetzner mit IMAP-Postfächern)                                                               |
| **Kalender**             | Outlook       | [Kalender](https://apps.nextcloud.com/apps/calendar)         | Synchronisiert per CalDAV bei mir mit [Thunderbird](https://www.thunderbird.net) und iOS Mail App                                                                                         |
| **Notizbuch**            | Onenote       | [Dateien](https://nextcloud.com/files/)                      | Ich nutze einen Obsidian-Vault in meinen Dateien (Nachteil: synchronisiert nicht mit iOS)                                                                                                 |
| **Aufgabenmanagement**   | ToDo          | [Tasks](https://apps.nextcloud.com/apps/tasks)               | Aufgaben werden auch im Kalender gespeichert, ich greife z.B. von Thunderbird und iOS Erinnerungen darauf zu                                                                              |
| **Formulare, Umfragen**  | Forms         | [Forms](https://apps.nextcloud.com/apps/forms)               | Tut, was es soll, die Live-Präsentation und die Anzeige von QR-Codes wäre noch schön                                                                                                      |
| **Automatisierung**      | PowerAutomate | [Flow](https://nextcloud.com/de/flow/)                       | Nutze ich bisher noch nicht, steht aber auf meiner Liste                                                                                                                                  |
| **Chat, Videokonferenz** | Teams         | [Talk](https://nextcloud.com/de/Talk/)                       | Nutze ich im privaten Umfeld wenig, weil Chatgruppen meist iOS oder Signal sind; Videokonferenzen mit 1-2 handvoll Leuten geht gut                                                        |
| **Bookmarks**            | Edge          | [Bookmarks](https://apps.nextcloud.com/apps/bookmarks)       | In der Microsoft-Welt ist man an Browser und Profil gebunden, ich nutze Floccus auf Laptops und Mobilgeräten, um Bookmarks überall verfügbar zu haben                                     |
| **Whiteboard**           | Whiteboard    | [Whiteboard](https://apps.nextcloud.com/apps/whiteboard)     | Ist bei Nextcloud ein eingebettetes [Excalidraw](https://de.wikipedia.org/wiki/Excalidraw), nutze ich aber bisher nicht                                                                   |
| **KI-Assistent**         | Copilot       | [Assistant](https://nextcloud.com/de/assistant/)             | Vorteil Nextcloud: es können beliebige KI-Dienste eingebunden werden (ich nutze [Openrouter](https://openrouter.ai/)); Nachteil: man muss sich separat um Datenschutz/-sicherheit kümmern |

**Was mir an Nextcloud fehlt:** man merkt, dass Nextcloud - wie früher Microsoft - sehr stark um Dokumente herum gebaut ist. Wo Microsoft mit den Sharepoint Communication Sites in Richtung Websites gegangen ist, gibt es im Nextcloud-Ökosystem kaum Ansätze. Es gibt "Pflänzchen" wie [Collectives](https://apps.nextcloud.com/apps/collectives) und [Cristal](https://apps.nextcloud.com/apps/cristal), die sind für mich bisher aber noch keine vollwertige Alternative. Webseiten, Weblogs, Microblogs & Co. muss man also bis jetzt noch in anderen Tools realisieren (dieser Blog ist mit [Markdown](https://de.wikipedia.org/wiki/Markdown), [mkdocs](https://www.mkdocs.org/) erstellt und auf [Github Pages](https://docs.github.com/de/pages) gehostet). Das ist in meinem Augen eine der größten Schwächen von Nextcloud als Ersatz zu Microsoft 365 z.B. in Intranets oder für Webseiten.

**Viel Spaß und Erfolg beim Ausprobieren!**