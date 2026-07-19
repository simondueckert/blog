---
date: 2026-07-19
categories:
   - Digitalität
tags:
   - Weblog
   - Mobiles Arbeiten
   - iOS
draft: false
---

# Mobiles Publizieren im Blog

Ob ich in meinem Blog etwas publiziere oder nicht hängt oft einfach davon ab, wie einfach es in der jeweiligen Situation ist. Mit dem Umstieg von Wordpress auf einen statischen Seitengenerator ist das schon deutlich einfacher geworden. Jetzt arbeite ich an Optionen für das Schreiben und Publizieren von iPhone und iPad (mit und ohne Netzwerk).

<!-- more -->

Zum **Schreiben auf iPad und iPhone** habe ich das [Universable Foldable Keyboard](https://www.galaxus.de/de/s1/product/microsoft-universal-foldable-keyboard-de-kabellos-tastatur-5646784) von Microsoft, das ich immer im Rucksack habe. Die Tastatur kann man zusammenklappen und per Bluetooth mit bis zu drei Geräten koppeln.

Die Inhalte meine Weblogs liegen in einem **Github Repository** und werden über **Github Pages** als Website ausgeliefert. Die Konvertierung von Markdown in statisches HTML übernimmt mkdocs (in Zukunft evtl. zensical) automatisch per **Github Action**.

Um das Github Repository mit den mobilen Geräten synchronisieren zu können, habe ich mich für die App [Working Copy](https://workingcopy.app) entschieden. Die hat einen eingebauten Editor, der reine Textdatei anzeigen kann und zusätzlich **Markdown-Syntax-Highlighting und -Vorschau** kann. Mehr brauche ich meist zum Schreiben nicht. Wenn ich doch Mal einen komfortablen WYSIWYG-Editor brauche, verwende ich [iA Writer](https://ia.net/de/writer), der auf das lokale Github-Repository zugreifen kann.

**Mkdocs mit dem Material-Theme** unterstützt neben reinem Markdown [eine Menge von Formatierungen](https://squidfunk.github.io/mkdocs-material/reference/), die ich in Zukunft etwas mehr nutzen möchte. Dazu gehören z.B. Admonitions und [Mermaid-Diagramme](https://mermaid.js.org) (Content-as-Code-Ansatz, statt binärer Bild-Formate).

![](https://pxlfdde.fsn1.your-objectstorage.com/public/m/_v2/473206466218206708/b5862bd14-4506fa/ZF81u810ftR5/AEXlornVhweRUyr19Wm3o2aPQa5KIpwBYnD6N5Yt.jpg)

Was ich als nächstes Ausprobieren möchte: Das Quellverzeichnis meines Weblogs als Vault in [Obsidian](https://obsidian.md) öffnen. Da Obsidian meine Standard-Notiz-App ist und viele zunächst private Inhalte später öffentlich werden, würde das einen eleganten Prozess des Veröffentlichens ohne Medienbruch darstellen. Ich werde mir dazu mal das Plugin [Digital Garden](https://community.obsidian.md/plugins/digitalgarden) ansehen, das ich auf dem letzten [IndieWebCamp in Nürnberg](https://indieweb.org/Nuremberg) kennengelernt habe.