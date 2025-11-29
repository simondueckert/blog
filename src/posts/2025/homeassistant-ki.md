---
date: 2025-11-29
categories:
  - smarthome
  - homeassistant
  - voice
  - projekt
draft: false
---

# Neues Projekt: Smarthome mit KI und Sprache nutzen
![](./images/homeassistant-ki.png)

Als **Smart-Home-System** für die **Automatisierung** von Lichtern, Musik, Heizung etc. verwende ich zu Hause [Homeassistant](https://www.home-assistant.io/) (früher habe ich [OpenHAB](https://www.openhab.org/) verwendet). Zum Kneten der ganzen Plätzchenteige haben wir uns jetzt endlich auch mal [eine Küchenmaschine](https://amzn.to/4otUzYv) gekauft. Die Anleitung umfasst über 200 Seiten und da liegt es nahe, **mit der Anleitung in der Küche auch "sprechen"** zu können.
<!-- more -->
Ich werde **über die Vorweihnachtszeit mal ein kleines Projekt** starten, um direkt in der Küche mit der Anleitung der Maschine (und natürlich auch allen anderen Anleitungen, Rezeptsammlung, Kochbücher etc.) "reden" zu können.

Dafür habe ich mir **folgenden Ansatz** überlegt:

1. Als erstes muss ich meinem Homeassistant das **Zuhören und Sprechen** beibringen. Zum Glück hatte ich mir vor einiger Zeit schon die [Preview Edition von Home Assistant Voice](https://www.home-assistant.io/voice-pe/) bestellt, die werde ich jetzt aktivieren.
2. Als **Text-to-Speech-System** (TTS) will ich [Piper](https://github.com/rhasspy/piper) einsetzen, das wollte ich mir zur Synthese von Tonspuren aus Texten ohnehin schon lange mal ansehen. Für englisch gibt es eine große Auswahl freier Stimmen, für deutsche Ausgabe werde ich mal die [Thorsten Voice](https://www.thorsten-voice.de/) ausprobieren.
3. Die Anleitungen liegen wie alle anderen **Dokumente** von uns in einer lokalen Instanz von [Paperless-ngx](https://docs.paperless-ngx.com/). Die muss an Homeassistant und das LLM angebunden werden.
4. Als **Sprachmodell** möchte ich was kleines verwenden, z.B. [Gemma3](https://ai.google.dev/gemma/docs/core?hl=de) 7B, zunächst über Openrouter, damit es schnell geht, später evtl. lokal auf einem [Mac Mini M4](https://amzn.to/3MdWC5j).
5. Idealerweise kann ich das Interface dann auch Richtung **Apple Home** "durchreichen", damit man es auch über das Smartphone gut ansprechen kann - habe nicht vor, in alle Räume Voice-Assistants zu stellen, auch wenn ich nicht wie Alexa die Angst haben, belauscht zu werden ;-)

Wenn das mal einigermaßen läuft, werde ich den Blog-Beitrag hier aktualisieren. Falls jemand Erfahrungen damit hat oder mitlernen will, gerne in die Kommentare schreiben.

P.S.: Florian hatte in der [pke25](https://cogneon.de/pke25) die Idee, die Blog-Beiträge lokal mit [Obsidian](https://obsidian.md) zu schreiben. Dieser Beitrag ist so entstanden und das hat super funktioniert. Ich brauche keinen extra Editor dafür und ich kann bei Bedarf die KI in Obsidian verwenden. Danke!