---
template: post
title: "IvyDE, usando repositorios Ivy desde Eclipse"
date: 2010-02-06
tags:
 - Eclipse
 - IvyDE
 - Ivy
---

Una vez creado nuestro repositorioIvy, usarlo con el plugin de Eclipse, [IvyDE](http://ant.apache.org/ivy/ivyde/), no es complicado.
La manera más sencilla de [instalarlo](http://ant.apache.org/ivy/ivyde/history/latest-milestone/install.html) es configurar el sitio de
actualización para Eclipse.

Una vez instalado, para usarlo en un proyecto solo necesitamos dos ficheros de configuración:`ivysettings.xml`y `ivy.xml`.
El fichero `ivysettings.xml` le indica a Ivy como usar nuestro repositorio configurando un resolver:

	<ivysettings>
		<settings defaultResolver="my-repository" />
		<resolvers>
			<filesystem name="my-repository">
				<ivy pattern="/home/miguel/repositorio-ivy/repository/[organisation]/[module]/ivys/ivy-[revision].xml"/>
				<artifact pattern="/home/miguel/repositorio-ivy/repository/[organisation]/[module]/[type]s/[artifact]-[revision].[ext]"/>
			</filesystem>
		</resolvers>
	</ivysettings>

En el `ficheroivy.xml` configuramos las dependencias de nuestro proyecto. Con el siguiente fichero de ejemplo configuro el proyecto para usar Spring:

	<?xml version="1.0" encoding="UTF-8"?>
	<ivy-module version="1.0">
		<info organisation="enlosdetalles.net" module="prueba_ivy" status="integration" />
		<dependencies>
			<dependency org="org.springframework" name="org.springframework.spring-library" rev="2.5.6.A" /> 
		</dependencies>
	</ivy-module>

Ahora solo falta decirle a IvyDE que nos haga el trabajo sucio. Lo primero es configurar en IvyDE con la ruta del fichero `ivysettings.xml`.

[![](http://dl.dropbox.com/u/302696/blog_files/ivyde/ivyde-settings.png)](http://dl.dropbox.com/u/302696/blog_files/ivyde/ivyde-settings.png)

Para [crear un "classpath container"](http://ant.apache.org/ivy/ivyde/history/latest-milestone/cpc/create.html) hacemos clic con el botón derecho del ratón en el fichero `ivy.xml` y seleccionamos "Add Ivy Library...". Es lo que el manual de IvyDE llama creación rápida.

[![](http://dl.dropbox.com/u/302696/blog_files/ivyde/ivyde-add-library.png)](http://dl.dropbox.com/u/302696/blog_files/ivyde/ivyde-add-library.png)

Y listo ya tenemos nuestro proyecto configurado con sus dependencias:

[![](http://dl.dropbox.com/u/302696/blog_files/ivyde/ivyde-classpath.png)](http://dl.dropbox.com/u/302696/blog_files/ivyde/ivyde-classpath.png)
