---
template: post
title: "Distribución de Skins de Apache Trinidad en Ficheros JAR"
date: 2009-09-20
tags:
 - Apache Trinidad
 - JSF
 - Skinning
---

Imagina que tenemos un skin de Apache Trinidad que queremos reutilizar en varias aplicaciones y además tenemos la necesidad de añadir estilos específicos de cada aplicación. ¿Cómo lo hacemos?

Para distribuir y compartir un skin en un fichero JAR hacemos lo siguiente:

1\. En el directorio `META-INF` creamos el fichero `trinidad-skin.xml`. Este fichero define el skin y Apache Trinidad lo busca en la carpeta `META-INF` de los ficheros JAR del classpath.

El contenido del fichero será el siguiente:

	<?xml version="1.0" encoding="ISO-8859-1"?>
	<skins xmlns="http://myfaces.apache.org/trinidad/skin">
		<skin>
			<id>MySkin.desktop</id>
			<family>MySkin</family>
			<render-kit-id>org.apache.myfaces.trinidad.desktop</render-kit-id>
			<style-sheet-name>skins/myskin-desktop.css</style-sheet-name>
		</skin>
	</skins>

2\. Como vemos en el contenido del fichero `trinidad-skin.xml`, el fichero CSS con los estilos de nuestro skin, `myskin-desktop.css` lo ubicamos también dentro de la carpeta `META-INF` en la carpeta skins.

3\. Las imágenes usadas en el skin las guardamos en la carpeta `META-INF/adf/images/myskin`. En el fichero de estilos hacemos referencia a las imágenes usando la ruta `../adf/images/myskin`, como se muestra en el siguiente ejemplo:

	af|messages::error-icon {
		content: url('../adf/images/myskin/dialog-error.gif');
	}

Una vez creado el fichero `mytrinidadskin.jar`, para usarlo en una aplicación sólo tenemos que colocarlo en el classpath y configurar la aplicación realizando lo siguiente:

1\. Modificar el fichero `trinidad-config.xml` para indicar a Apache Trinidad que use nuestro skin:

	<?xml version="1.0"?>
		<trinidad-config xmlns="http://myfaces.apache.org/trinidad/config">
		<skin-family>MySkin</skin-family>
	</trinidad-config>

2\. Para que Apache Trinidad recupere correctamente las imágenes tiene que estar configurado el Trinidad Resource Servlet en el fichero `web.xml`.

	<servlet>
		<servlet-name>Trinidad Resources Servlet</servlet-name>
		<servlet-class>org.apache.myfaces.trinidad.webapp.ResourceServlet</servlet-class>
	</servlet>

	<servlet-mapping>
		<servlet-name>Trinidad Resources Servlet</servlet-name>
		<url-pattern>/adf/*</url-pattern>
	</servlet-mapping>

Ya tenemos nuestro skin en un fichero JAR y una aplicación configurada para usarlo, ahora necesitamos añadir los estilos específicos de la aplicación.

Para esto en el directorio `WEB-INF` de nuestra aplicación creamos el directorio `skins` que contendrá el fichero `myapplicacion-desktop.css`. Además en el directorio `WEB-INF` creamos el fichero `trinidad-skin.xml` con el siguiente contenido:

	<?xml version="1.0" encoding="ISO-8859-1"?>
	<skins xmlns="http://myfaces.apache.org/trinidad/skin">
		<skin-addition>
 			<skin-id>MySkin.desktop</skin-id>
			<style-sheet-name>/WEB-INF/skins/myapplication-desktop.css</style-sheet-name>
		</skin-addition>
	</skins>

De esta forma los estilos de la aplicación se añaden al skin MySkin que hemos distribuido en el fichero JAR.

**Enlaces de interés.**

* [Custom skins deployment strategies.](http://thepeninsulasedge.com/frank_nimphius/2008/02/06/custom-skins-deployment-strategies-for-myfaces-trinidad-and-adf-faces-rich-client/)

* [Apache Trinidad Skinning.](http://myfaces.apache.org/trinidad/devguide/skinning.html)
