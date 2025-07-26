---
title: "Eine neue Chat-Plattform für die Cogneon Akademie"
date: 2020-12-20
categories: 
  - "cogneon"
  - "infrastruktur"
  - discord
  - slack
  - rocketchat
---

Neben unserer Community-Plattform [CONNECT](https://community.cogneon.de) auf Basis von Discourse braucht es für den schnellen Austausch zwischendurch eine geeignete Chat-Plattform. Hier haben wir in den letzten beiden Jahren einige Experimente gemacht und daraus gelernt. Im Jahr 2019 haben wir [IRC](https://de.wikipedia.org/wiki/Internet_Relay_Chat) auf dem Server [Freenode](https://freenode.net/) getestet. IRC wird im Hackerumfeld viel genutzt. Gut an IRC finde ich den offenen Umgang mit Chat-Kanälen (jeder kann neue Kanäle anlegen, Kanäle sind i.d.R. offen). Eine Funktion, die ich von keiner anderen Chat-Plattform kenne ist, dass angezeigt wird, wenn jemand den Kanal betritt und wenn er wieder geht. So bekommt man ein gutes Gefühl, wer gerade "da" ist. Allerdings hat IRC nie so richtig den Weg in den Web 2.0 und Mobile Welt geschafft, die Nutzung fühlt sich an vielen Ecken und Enden etwas altbacken an.

<!-- more -->

In 2020 sind wir dann von IRC auf [Discord](https://de.wikipedia.org/wiki/Discord_\(Software\)) gewechselt. Discord hat sich im Gaming-Bereich als Text- und Audio-Chat-Plattform etabliert. Auf Discord legt man sich einen eigenen "Server" an, der ist aber Cloud-basiert und muss (kann) nicht selber gehostet werden. Besonderheit von Discord ist, dass es neben Text auch qualitativ hochwertigen Audio-Chat anbietet. Außerdem ist Video-Chat/Screensharing mit bis zu 9 Personen möglich. Der Discord-Server wurde zwar deutlich mehr genutzt, als IRC, hat sich aber auch in der Community nicht wirklich etabliert. Ich vermute Discord ist zu "nischig" und im Arbeitsalltag der meisten zu wenig präsent.

Beim [lernOS All Stars Camp 2020](https://cogneon.de/loscamp20/) haben wir [Telegram](https://de.wikipedia.org/wiki/Telegram) als übergreifenden Chat verwendet (als Veranstaltungsplattform haben wir ein Dokuwiki verwendet). Für eine Veranstaltung funktioniert das auch sehr gut. Über einen Gruppen-Beitrittslink kann man alle Teilnehmenden bequem einladen, ohne explizites User Management betreiben zu müssen. Für ein einzelnes Event hat das auch sehr gut funktioniert. In einer Community gibt es aber immer auch Teilprojekte/-themen für die eine einzelne Chat-Gruppe zu "eng" ist. Es braucht die Möglichkeit, mehrere Chat-Kanäle anzulegen und zu verwalten, da sonst weitere Telegram-Gruppen und damit Intransparenz und Silos entstehen.

Idee für 2021 war also, ein **Multi-Channel-Chat-Tool** auszuprobieren. Dazu habe ich auf Twitter eine kleine Umfrage durchgeführt, bei der 116 Personen abgestimmt haben.

Zur Auswahl standen Telegram, Slack, Discord und Rocket.Chat als Chat-Tools. Slack hat dabei die Abstimmung mit einigem Abstand gewonnen:

- **Telegram:** 31,0%
- **Slack:** 47,4%
- **Discord:** 13,8%
- **Rocket.Chat**: 7,8%
- **Andere (Kommentare):** Matrix, Threema, XMPP, iMessage, WhatsApp, Signal

Für **2021** werden wir also auf **Slack** als Chat-Plattform setzen. Dafür reaktivieren wir das Netzwerk, das wir auch schon in unseren Benchlearning-Projekten verwendet haben. Einen ersten Test machen wir bei unserem virtuellen Wintermarkt am 21.12.2020, danach laden wir alle Nutzer\*innen von Discord und CONNECT in das Netzwerk ein.

P.S.: mir wäre eigentlich [Rocket.Chat](https://rocket.chat/) als Open-Source-Alternative zu Slack lieber gewesen. Im Chaos Computer Club setzen wir das gerade für die Planung der [Remote Chaos Experience rC3](https://rc3.world) ein und an Funktionen fehlt mir da gegenüber Slack nichts. Zwei Probleme: 1.) Das nutzen in unserer Community vermutlich sehr wenige und wir hätten das gleiche Problem, wie bei Discord 2.) Wir hätten eine weitere Plattform, die wir selber hosten müssen und das wollte ich nicht. Die Bezahl-Variante bei Rocket ist leider 3,-/User/Monat, was bei eier Community mit 1.500+ Leuten nicht finanzierbar ist.
