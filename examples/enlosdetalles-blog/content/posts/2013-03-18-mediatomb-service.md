---
template: post
title: "MediaTomb, espera un poquito por favor."
date: 2013-03-18
tags:
 - GNU/Linux
 - MediaTomb
---

[MediaTomb](http://mediatomb.cc/) es un servidor multimedia de código abierto.

El servicio de MediaTomb (en mi Ubuntu 12.10) no arranca correctamente y en el log vemos los siguientes errores:

	2013-03-13 18:44:52   ERROR: Could not determine interface address: Cannot assign requested address
	2013-03-13 18:44:52   ERROR: Could not find interface: wlan0

El problema se produce porque he configurado MediaTomb para que use la interfaz wifi `wlan0`, pero cuando arranca todavía no está disponible.

Para conseguir que MediaTomb no arranque hasta que no haya red wifi modificamos el fichero de configuración del servicio upstart `/etc/init/mediatom.conf`. [Cambiamos](https://gist.github.com/msosvi/5190490/revisions) la condición de arranque `IFACE!=lo` por `IFACE=wlan0`.
