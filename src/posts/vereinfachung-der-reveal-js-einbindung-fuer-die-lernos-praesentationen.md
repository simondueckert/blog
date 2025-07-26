---
title: "Vereinfachung der reveal.js Einbindung für die lernOS Präsentationen"
date: 2019-09-22
categories: 
  - "lernos"
  - "revealjs"
---

Zu den **lernOS Leitfäden** soll es jeweils eine **begleitende Präsentation** geben, mit der man den Leitfaden vorstellen und Dojos (Workshops) durchführen kann. Um nicht von Desktop-Anwendungen (PowerPoint, Keynote, Impress) abhängig zu sein, haben wir uns für das HTML Presentation Framework [reveal.js](https://revealjs.com/) entschieden. Nach der Anleitung von #revealjs kann man sich die ganzen Quellen herunterladen, in ein Verzeichnis entpacken und von dort per index.html starten. Das habe ich inkl. des Uploads in das docs Verzeichnis von GitHub für die Generierung der [GitHub Pages](https://pages.github.com/) mit Erfolg probiert.

<!-- more -->

Nachteil ist, dass die ganzen **Quellen von reveal.js** (CSS, JavaScript, Plugins etc.) auch im GitHub Repository verwaltet werden müssen. Daher habe ich einen anderen Weg gesucht und gefunden. Alle Quellen von reveal.js werden auch über Open Source [Content Delivery Networks](https://de.wikipedia.org/wiki/Content_Delivery_Network) (CDN) wie beispielsweise [cdnjs.com](https://cdnjs.com/) angeboten. Auf diesem Weg kann man immer die aktuelle Version des Frameworks verwenden und die Auslieferung der Dateien erfolgt auch noch deutlich schneller.

In der **index.html** sind dafür nur folgende Änderungen vorzunehmen:

```
**Alt:** \[code\] <link rel="stylesheet" href="css/reset.css"> <link rel="stylesheet" href="css/reveal.css"> <link rel="stylesheet" href="css/theme/league.css"> <script src="js/reveal.js"></script> \[/code\]

**Neu:** \[code\] <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.8.0/css/reset.min.css"> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.8.0/css/reveal.min.css"> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.8.0/css/theme/league.min.css"> <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.8.0/js/reveal.js"></script> \[/code\]
```

Somit muss im GitHub-Repository nur noch die Datei index.html verwaltet werden, der ganze Rest kommt vom CDN. Um weitere Bandbreite zu sparen, habe ich gleich die [minifizierten](https://wiki.selfhtml.org/wiki/Minify) CSS-Dateien eingebunden. Die unkomprimierten Dateien sind [im Bereich reveal.js auf dem CDN](https://cdnjs.com/libraries/reveal.js) aber auch verfügbar.

Die Präsentation zum #lernOS for You Leitfaden ist aktuell nur [im Development Branch](https://github.com/cogneon/lernos-for-you/tree/develop) verfügbar. Da die Quellen für GitHub Pages immer im Verzeichnis "/docs" im Master Branch liegen müssen, ist mir noch nicht klar, wie wir mit Sprachversionen bei Leitfäden umgehen, die mehrsprachig verfügbar sind. Ich habe den neuen Ansatz jetzt erstmal mit der deutschen Version der Präsentation umgesetzt und werde mir demnächst noch ein kleines Konzept zur Mehrsprachigkeit überlegen (Bilder und Farben fehlen noch):

https://github.com/cogneon/lernos-for-you/tree/master/docs https://cogneon.github.io/lernos-for-you
