---
template: post
title: "Cómo instalar varias versiones de Firefox en Ubuntu"
date: 2010-08-14
tags:
 - VMWare
 - GNU/Linux
 - Firefox
---

La consola remota de VMWare 2 tiene un problema con la versión 3.6. de Firefox. Una solución es instalar Firefox 3.5. y usarlo para acceder al servidor VMWare.

Para instalar otra versión en Ubuntu hacemos más o menos lo que explican [aquí](http://www.wikihow.com/Install-multiple-versions-of-Firefox-on-Ubuntu):

1. Descargamos la versión de [http://www.mozilla.com/en-US/firefox/all-older.html]().

2. Creamos la carteta `/opt/firefox35` y descomprimimos el fichero (en mi caso `firefox-3.5.11.tar.bz2`) dentro.

3. Arrancamos el administrador de perfiles con el comando `/opt/firefox35/firefox -ProfileManager`  y creamos un nuevo perfil llamado `Firefox35`.

4. Para usar el `Firefox35` lo arrancamos con el comando `/opt/firefox/firefox -no-remote -P "Firefox35"`.


