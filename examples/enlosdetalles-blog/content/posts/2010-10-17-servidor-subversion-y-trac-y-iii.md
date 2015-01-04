---
template: post
title: "Servidor Subversion y Trac (y III). Instalación de Trac."
date: 2010-10-17
tags:
 - Subversion
 - Trac
 - GNU/Linux
---

Y ahora el último paso, la instalación y configuración de [Trac](http://es.wikipedia.org/wiki/Trac). 

Para instalar Trac ejecuto los siguientes comandos:

	$ sudo apt-get install libapache2-mod-python python-setuptools python-subversion
	$ sudo easy_install Trac
	$ sudo mkdir /var/trac
	$ sudo chown www-data:www-data /var/trac 
	
Para configurar Apache añado al fichero `/etc/apache2/sites-available/trac` lo siguiente:

	<virtualhost *>
		ServerAdmin webmaster@localhost
		ServerName trac.example.com
		DocumentRoot /var/www
		ErrorLog /var/log/apache2/error.trac.log
		CustomLog /var/log/apache2/access.trac.log combined

		<location /trac >
			SetHandler mod_python
			PythonInterpreter main_interpreter
			PythonHandler trac.web.modpython_frontend
			PythonOption TracEnvParentDir /var/trac
			PythonOption TracUriRoot /trac
			PythonOption PYTHON_EGG_CACHE /tmp
			PythonOption TracLocale "es_ES.UTF-8"
		</Location>

		<LocationMatch "/trac/[^/]+/login">
			AuthType Basic
			AuthName "trac"
			AuthUserFile /etc/apache2/dav_svn.passwd
			Require valid-user
		</LocationMatch>
	</virtualHost>

A continuación deshabilito el servidor virtual por defecto de Apache, habilito el de Trac y reinicio Apache:

	$ sudo a2dissite default
	$ sudo a2ensite trac
	$ sudo /etc/init.d/apache2 reload
	
Para crear un nuevo proyecto Trac uso el comando:

	$ sudo trac-admin /var/trac/proyecto1 initenv
	
A partir de la versión 0.12 de Trac este comando no hace preguntas sobre la configuración del control de versiones. La configuración de los repositorios, en mi caso de Subversión, se hace modificando el fichero `trac.ini` y añadiendo las sección `repositories`:

	[repositories] 
	protecto1.dir=/var/svn/proyecto1 
	proyecto1.type=svn 
	.alias = proyecto1 
	.hidden = true
	
En esta configuración indico el directorio del repositorio, el tipo. También lo configuro como repositorio por defecto (propiedades `.alias` y `.hidden`), esto hace falta ya que Trac está configurado para comprobar automáticamente los nuevos commits sólo del repositorio por defecto.

Por último le doy permiso al usuario `miguel` para acceder al menú de administración de Trac usando el comando

 $ sudo trac-admin /var/trac/proyecto1 permission add miguel TRAC_ADMIN
 
Para actualizar proyectos Trac de versiones anteriores, además de añadir al `trac.ini` la configuración de los repositorios, ejecuto el comando:

	$ sudo trac-admin /var/trac/proyecto2 upgrade
	
También será necesario resincronizar el repositorio de Subversion:

	$ sudo trac-admin /var/trac/proyecto2 repository resync proyecto2
	
**Todas las entradas de la serie:**

* [Servidor Subversion y Trac (I). Instalación de Ubuntu Server.](http://www.enlosdetalles.net/2010/08/servidor-subversion-y-trac-i.html)
* [Servidor Subversion y Trac (II). Instalación de Subversion.](http://www.enlosdetalles.net/2010/09/servidor-subversion-y-trac-ii.html)
* [Servidor Subversion y Trac (y III). Instalación de Trac.](http://www.enlosdetalles.net/2010/10/servidor-subversion-y-trac-y-iii.html)
