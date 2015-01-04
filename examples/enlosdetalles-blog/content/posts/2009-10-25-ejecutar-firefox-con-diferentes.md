---
template: post
title: "Ejecutar Firefox con Diferentes Perfiles"
date: 2009-10-25
tags:
 - Firefox
---

Para probar aplicaciones web, muy a menudo necesito ejecutar Firefox con dos perfiles distintos y poder validarme en la aplicación con dos usuarios también distintos.

En condiciones normales, por muchas ventanas que abramos de Firefox, siempre se usará el perfil por defecto, y las cookies de sesión de mi aplicación serán comunes a todas las ventanas.

Lo primero que tenemos que hacer es crear otro perfil ejecutando:

	$ firefox -profilemanager

En mi caso he creado un nuevo perfil 'Miguel'.

[![](http://dl.getdropbox.com/u/302696/blog_files/firefox-sessions/Pantallazo-Firefox%20-%20Choose%20User%20Profile.png)](http://dl.getdropbox.com/u/302696/blog_files/firefox-sessions/Pantallazo-Firefox%20-%20Choose%20User%20Profile.png)

Si arranco Firefox sin más parámetros, usará el perfil por defecto.
Y si desde el terminal ejecuto:

	$ firefox -P Miguel -no-remote

ya tengo mi segunda sesión de Firefox con el perfil Miguel.
