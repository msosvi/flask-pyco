---
template: post
title: "Servidor Subversion y Trac (II). Instalación de Subversion."
date: 2010-09-08
tags:
 - Subversion
 - GNU/Linux
---

[Una vez instalado el servidor Ubuntu](http://www.enlosdetalles.net/2010/08/servidor-subversion-y-trac-i.html), instalo y configuro Subversion. Para instalar Subversion en mi servidor y crear un reporsitorio ejecuto los siguientes comandos:

	$ sudo apt-get install subversion libapache2-svn
	$ sudo mkdir /var/svn
	$ cd /var/svn
	$ sudo svnadmin create proyecto1
	$ sudo chown www-data:www-data /var/svn/ -R
	
	
Para configurar el servidor Apache para acceder a los repositorios de Subversion lo más sencillo es editar el fichero `/etc/apache2/mods-available/dav_svn.conf` y añadir:

	<location /svn/ >
		DAV svn
		SVNParentPath /var/svn/
		
		AuthType Basic
		AuthName "My Repository"
		AuthUserFile /etc/apache2/dav_svn.passwd
		
		Require valid-user
	</location>
	
El fichero `/etc/apache2/dav_svn.passwd` es un fichero de claves de Apache. Para crear el fichero y añadir un usuario uso el comando `htpasswd`. Después reinicio el servidor web:

	$ sudo htpasswd -c /etc/apache2/dav_svn.passwd miguel
	$ sudo apache2ctl restart
	
Ahora ya puedo acceder al repositorio del proyecto en la dirección `http://miservidor/svn/proyecto1`

**Todas las entradas de la serie:**

* [Servidor Subversion y Trac (I). Instalación de Ubuntu Server.](http://www.enlosdetalles.net/2010/08/servidor-subversion-y-trac-i.html)
* [Servidor Subversion y Trac (II). Instalación de Subversion.](http://www.enlosdetalles.net/2010/09/servidor-subversion-y-trac-ii.html)
* [Servidor Subversion y Trac (y III). Instalación de Trac.](http://www.enlosdetalles.net/2010/10/servidor-subversion-y-trac-y-iii.html)
