---
template: post
title: "Servidor Subversion y Trac (I). Instalación de Ubuntu Server."
date: 2010-08-22
tags:
 - VMWare
 - GNU/Linux
---

Voy a describir los pasos que usé para instalar un servidor [Subversion](http://es.wikipedia.org/wiki/Subversion) y [Trac](http://es.wikipedia.org/wiki/Trac).

El primer paso es instalar un Ubuntu Server 10.4. La instalación, en mi caso como una maquina virtual de VMWare, es muy rápida y sencilla. En la selección de programas marco los servidores LAMP y OpenSSH.

Una vez terminada sólo tuve dos problemas con el teclado. En primer lugar no se mostraban bien los acentos y la ñ. Esto lo solucioné ejecutando el comando:

	$ sudo dpkg-reconfigure console-setup
	
Además no funcionaban algunas teclas como el Alt-Gr o los cursores. Esto es un problema de VMWare que solucioné añadiendo al fichero `/etc/vmware/config` las siguientes lineas:

	xkeymap.keycode.108 = 0x138 # Alt_R
	xkeymap.keycode.106 = 0x135 # KP_Divide
	xkeymap.keycode.104 = 0x11c # KP_Enter
	xkeymap.keycode.111 = 0x148 # Up
	xkeymap.keycode.116 = 0x150 # Down
	xkeymap.keycode.113 = 0x14b # Left
	xkeymap.keycode.114 = 0x14d # Right
	xkeymap.keycode.105 = 0x11d # Control_R
	xkeymap.keycode.118 = 0x152 # Insert
	xkeymap.keycode.119 = 0x153 # Delete
	xkeymap.keycode.110 = 0x147 # Home
	xkeymap.keycode.115 = 0x14f # End
	xkeymap.keycode.112 = 0x149 # Prior
	xkeymap.keycode.117 = 0x151 # Next
	xkeymap.keycode.78 = 0x46 # Scroll_Lock

Para usar el servidor con un poco de comodidad si fuera necesario, instalé un entorno gráfico mínimo.

	$ sudo apt-get install xorg gnome-core
	$ sudo apt-get install gksu
	$ sudo apt-get install gnome-themes-selected
	$ sudo apt-get install firefox
	
	
Ahora cuando necesito usar el entorno gráfico sólo tengo que usar el comando `startx`

**Todas las entradas de la serie:**

* [Servidor Subversion y Trac (I). Instalación de Ubuntu Server.](http://www.enlosdetalles.net/2010/08/servidor-subversion-y-trac-i.html)
* [Servidor Subversion y Trac (II). Instalación de Subversion.](http://www.enlosdetalles.net/2010/09/servidor-subversion-y-trac-ii.html)
* [Servidor Subversion y Trac (y III). Instalación de Trac.](http://www.enlosdetalles.net/2010/10/servidor-subversion-y-trac-y-iii.html)

