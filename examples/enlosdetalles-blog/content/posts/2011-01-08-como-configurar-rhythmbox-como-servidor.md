---
template: post
title: "Cómo configurar RhythmBox como servidor UPnP/DLNA"
date: 2011-01-08
tags:
 - GNU/Linux
 - RhythmBox
---

Instalamos el plugin de RhythmBox para compartir nuestra música con UPnP/DLNA usando el siguiente comando:

	$ sudo apt-get install rhythmbox-plugin-coherence

Ejecutamos RhythmBox, abrimos la ventana de los complementos y activamos el complemento "Soporte para control y comparticiones DNLA/UPnP".

[![](http://dl.dropbox.com/u/302696/blog_files/rythmbox_dnla/configurar_complementos.png)](http://dl.dropbox.com/u/302696/blog_files/rythmbox_dnla/configurar_complementos.png)

Pulsando el botón "Configurar" añadimos el puerto (49153 es el puerto por defecto de DNLA) y la interfaz de red (wlan0 si queremos usar la wifi).

[![](http://dl.dropbox.com/u/302696/blog_files/rythmbox_dnla/DLNA-UPnP_configuration.png)](http://dl.dropbox.com/u/302696/blog_files/rythmbox_dnla/DLNA-UPnP_configuration.png)

**Recursos:**

* [RhythmBox - Coherence - a DLNA/UPnP Framework for the Digital Living - Trac](http://coherence.beebits.net/wiki/RhythmBox)
