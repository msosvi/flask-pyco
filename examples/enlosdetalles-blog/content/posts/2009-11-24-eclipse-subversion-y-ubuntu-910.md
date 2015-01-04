---
template: post
title: "Eclipse, Subversion y Ubuntu 9.10."
date: 2009-11-24
tags:
 - Subclipse
 - Eclipse
 - Ubuntu
---

Después de actualizar Ubuntu a la versión 9.10. tuve algunos problemas con Eclipse.

Lo primero es que algunos botones de Eclipse dejaron de responder al pulsarlos con el ratón. De este problema ya estaba prevenido por 
[DiarioLinux](http://diariolinux.com/2009/11/18/eclipse-ventanas-grises-y-la-gran-comunidad/) y como indican en 
[este blog](http://www.norio.be/blog/2009/10/problems-eclipse-buttons-ubuntu-910) añado a mi `eclipse.sh` la siguiente línea:

	export GDK_NATIVE_WINDOWS=1

El siguiente problema fue que Subclipse dejó de funcionar mostrando el siguiente error:

[![](http://dl.dropbox.com/u/302696/blog_files/eclipse_ubuntu_9_10/unable_load_svn_client.png)](http://dl.dropbox.com/u/302696/blog_files/eclipse_ubuntu_9_10/unable_load_svn_client.png)

Este problema se produce porque la actualización de Ubuntu deja Subversion en la versión 1.6.5. y la versión de Subclipse que tenía instalada, la 1.4., no es compatible. 

Me dispuse a actualizar Subclipse a la versión 1.6. pero Eclipse no hacía otra cosa que cerrarse de forma inesperada. Encuentro unos cuantos [bugs](https://bugs.launchpad.net/ubuntu/+source/openjdk-6/+bug/445009) que hacen referencia a este problema y una solución: desactivar las tecnologías de asistencia (Sistema>Preferencias>Tecnologías de asistencia).

[![](http://dl.dropbox.com/u/302696/blog_files/eclipse_ubuntu_9_10/tecnologias_asistencia.png)](http://dl.dropbox.com/u/302696/blog_files/eclipse_ubuntu_9_10/tecnologias_asistencia.png)

Una vez solucionado esto, me dispongo a actualizar Sublipse. Después de algunos intentos lo consigo, pero usando el fichero 
site-1.6.5.zip, con la URL de actualización no va.

Hay que tener en cuenta que para que Subclipse encuentre la librería [JavaHL](http://subclipse.tigris.org/wiki/JavaHL) de Subversion hay que añadir la siguiente línea en el fichero `eclipse.sh`:

	export LD_LIBRARY_PATH=/usr/lib/jni

[![](http://dl.dropbox.com/u/302696/blog_files/eclipse_ubuntu_9_10/preferences_svn.png)](http://dl.dropbox.com/u/302696/blog_files/eclipse_ubuntu_9_10/preferences_svn.png)

Listo, parece que Eclipse ya se lleva bien con Ubuntu 9.10.
