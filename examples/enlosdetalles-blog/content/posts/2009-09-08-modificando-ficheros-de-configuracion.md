---
template: post
title: "Modificando ficheros de configuración con Ant y XMLTask"
date: 2009-09-08
tags:
 - Ant
 - XMLTask
---

Al crear el fichero war de una aplicación siempre hay que modificar, en los ficheros de configuración, valores necesarios durante el desarrollo y las pruebas, pero que no tienen sentido cuando la aplicación pasa a producción. Ejemplos de estas modificaciones son los niveles de log o depuración o la programación de tareas.

Si usamos Ant para generar nuestro fichero war, [XMLTask](http://www.oopsconsultancy.com/software/xmltask/) nos sirve para realizar estas modificaciones.

Para utilizar XMLTask añadimos la definición de la tarea en el fichero `build.xml` de Ant:

	<taskdef name="xmltask" classname="com.oopsconsultancy.xmltask.ant.XmlTask" />

Y ahora dos ejemplos de su uso, primero modifico en el descriptor de la aplicación web dos propiedades de Apache Trinidad usadas durante el desarrollo. También elimino los comentarios del fichero.

	<xmltask source="${webcontent.eclipse.dir}/${webxml.file}" dest="${config.dir}/${webxml.file}" failWithoutMatch="true">
		<replace path="/:web-app/:context-param[:param-name/text()='org.apache.myfaces.trinidad.CHECK_FILE_MODIFICATION']/:param-value/text()" withText="false" />
		<replace path="/:web-app/:context-param[:param-name/text()='org.apache.myfaces.trinidad.DISABLE_CONTENT_COMPRESSION']/:param-value/text()" withText="false" />
		<remove path="/:web-app/comment()" />
	</xmltask>

En el siguiente ejemplo modifico el fichero `persistence.xml` sustituyendo las propiedades de conexión a la base de datos:

	<xmltask source="${build.eclipse.dir}/classes/META-INF/persistence.xml"
		dest="${config.dir}/WEB-INF/classes/META-INF/persistence.xml" failWithoutMatch="true">
		<replace path="//:persistence/:persistence-unit/:properties">
 			<![CDATA[
				<properties xmlns="http://java.sun.com/xml/ns/persistence">
					<property name="eclipselink.jdbc.url" value="jdbc:oracle:thin:@oracleproduccion:1521:sid" />
					<property name="eclipselink.jdbc.driver" value="oracle.jdbc.driver.OracleDriver" />
					<property name="eclipselink.jdbc.user" value="user" />
					<property name="eclipselink.jdbc.password" value="password" />
					<!-- Provider-specific settings -->
					<!-- Configure EclipseLink internal connection pooling. -->
					<property name="eclipselink.jdbc.write-connections.min" value="3"/>
					<property name="eclipselink.jdbc.write-connections.max" value="7"/>
				</properties>
			]]>
		</replace>
	</xmltask>

**Enlaces de interés.**

 * [Página de XMLTask.](http://www.oopsconsultancy.com/software/xmltask)

 * [XML Manipulation using XMLTask.](http://today.java.net/pub/a/today/2006/11/01/xml-manipulation-using-xmltask.html)
