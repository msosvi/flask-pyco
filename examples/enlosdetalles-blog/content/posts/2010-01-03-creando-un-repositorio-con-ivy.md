---
template: post
title: "Creando un repositorio con Ivy"
date: 2010-01-03
tags:
 - Ant
 - Ivy
---

[Apache Ivy](http://ant.apache.org/ivy/) es un administrador de dependencias de librerías Java. Esta herramienta nos permite crear nuestro propio repositorio descargando las librerías y sus dependencias desde repositorios públicos de Maven o Ivy.

La [instalación](http://ant.apache.org/ivy/history/latest-milestone/install.html) de Ivy es sencilla, necesitamos instalar Ant, del que Ivy es un subproyecto, y un JDK (si al ejecutar ant se queja diciendo `Unable to locate tools.jar` es que falta instalar el JDK).

Creo la carpeta `/home/miguel/repositorio-ivy` para el repositorio. Dentro de esta creo la carpeta `settings` para guardar el fichero de configuración `ivysettings.xml`. En este fichero indico los repositorios públicos que voy a usar para recuperar las librerías y sus dependencias. El contenido del fichero es el siguiente:

~~~ xml
<ivysettings>
	<settings defaultResolver="com.springsource.repository"
		defaultConflictManager="all" />

		<!-- in order to get all revisions without any eviction -->
	<resolvers>
		<ibiblio name="libraries" m2compatible="true" />
		<ibiblio name="jboss" m2compatible="true"
			root="http://repository.jboss.org/maven2/" />

		<filesystem name="my-repository">
			<ivy pattern="${dest.repo.dir}/[organisation]/[module]/ivys/ivy-[revision].xml"/>
			<artifact pattern="${dest.repo.dir}/[organisation]/[module]/[type]s/[artifact]-[revision].[ext]"/>
		</filesystem>

		<chain name="com.springsource.repository" returnFirst="true">
			<url name="com.springsource.repository.bundles.release">
				<ivy pattern="http://repository.springsource.com/ivy/bundles/release/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
				<artifact pattern="http://repository.springsource.com/ivy/bundles/release/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
			</url>

			<url name="com.springsource.repository.libraries.release">
				<ivy pattern="http://repository.springsource.com/ivy/libraries/release/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
				<artifact pattern="http://repository.springsource.com/ivy/libraries/release/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
			</url>

			<url name="com.springsource.repository.bundles.external">
				<ivy pattern="http://repository.springsource.com/ivy/bundles/external/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
				<artifact pattern="http://repository.springsource.com/ivy/bundles/external/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
			</url>

			<url name="com.springsource.repository.libraries.external">
				<ivy pattern="http://repository.springsource.com/ivy/libraries/external/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
				<artifact pattern="http://repository.springsource.com/ivy/libraries/external/[organisation]/[module]/[revision]/[artifact]-[revision].[ext]" />
			</url>
		</chain>
	</resolvers>
</ivysettings>
~~~

Los distintos repositorios que voy a usar aparecen dentro de la etiqueta resolvers. Uso dos repositorios Maven configurados con en la etiqueta `ibiblio` y el [SpringSource Bundle Repository](http://www.springsource.com/repository/app/). 

En la [página de preguntas frecuentes](http://www.springsource.com/repository/app/faq) de repositorio de SpringSource nos indican como tenemos que
[configurar Ivy para trabajar con el repositorio](http://www.springsource.com/repository/app/faq#q7), hay que configurar cuatro resolvers. Para resolver correctamente algunas dependencias los configuro dentro de una etiqueta chain que permite usarlos conjuntamente.

Por supuesto también describo mi repositorio con la etiqueta `filesystem`.

Para añadir librerías en mi repositorio desde los repositorios públicos creo en el directorio `/home/miguel/repositorio-ivy` el fichero
`build.xml` de Ant. La tarea `ivy:install` nos permite copiar módulos y sus dependencias de un repositorio a otro.

Este es mi fichero `build.xml` con algunas de las librerías que necesito en mi repositorio (Myfaces, Spring, Spring Web Flow, Spring Security, Spring Batch, Apache Trinidad):

~~~ xml
<?xml version="1.0"?>
<!-- ======================================================================
 This is the project to build my own ivy repository.
 ====================================================================== -->

<project name="ivy-repository" xmlns:ivy="antlib:org.apache.ivy.ant">
	<property name="settings.dir" value="settings"/>
	<property name="dest.repo.dir" value="/home/miguel/repositorio-ivy/repository" />
	<property name="reports.dir" value="/home/miguel/repositorio-ivy/reports" />
	<property name="ivy.jar.file" value="${ivy.jar.dir}/ivy.jar" />
	<property name="ivy.cache.dir" value="${basedir}/cache" />

	<!-- target: init-ivy -->

	<target name="init-ivy" >
		<ivy:settings id="settings" file="${settings.dir}/ivysettings.xml"/>
	</target>

	<!-- target: install-modules and dependecies -->

	<target name="install-myfaces" depends="init-ivy" description="--> install Apache MyFaces and dependecies">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.apache.myfaces" module="com.springsource.org.apache.myfaces" revision="1.2.2"
			from="com.springsource.repository.bundles.external"
			to="my-repository"
			transitive="true" />
	</target>

	<target name="install-spring" depends="init-ivy" description="--> install Spring Framework and dependecies">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.springframework" module="org.springframework.spring-library" revision="2.5.6.A"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />
	</target>

	<target name="install-swf" depends="init-ivy" description="--> install Spring Web Flow and dependecies">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.springframework.webflow" module="org.springframework.webflow-library" revision="2.0.8.RELEASE"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />
	</target>

	<target name="install-spring-security" depends="init-ivy" description="--> install Spring Security and dependecies">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.springframework.security" module="org.springframework.security" revision="2.0.4.A"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />
	</target>

	<target name="install-spring-batch" depends="init-ivy" description="--> install Spring Batch and dependecies">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.springframework.batch" module="org.springframework.batch.core" revision="2.0.4.RELEASE"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />

		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.springframework.batch" module="org.springframework.batch.test" revision="2.0.4.RELEASE"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" /> <ivy:install settingsRef="settings" overwrite="true"
			organisation="org.springframework.batch" module="org.springframework.batch.infrastructure" revision="2.0.4.RELEASE"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />
	</target>

	<target name="install-trinidad" depends="init-ivy description="--> install Apache Trinidad and dependecies">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.apache.myfaces.trinidad" module="trinidad" revision="1.2.12"
			from="jboss"
			to="my-repository"
			transitive="true"
			haltonfailure="false"/>

		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.apache.myfaces.trinidad" module="trinidad-api" revision="1.2.12"
			from="jboss"
			to="my-repository"
			transitive="true" />

		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.apache.myfaces.trinidad" module="trinidad-impl" revision="1.2.12"
			from="libraries"
			to="my-repository"
			transitive="true" />
	</target>

	<target name="install-eclipselink" depends="init-ivy" description="--> install eclipselink">
		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.eclipse.persistence" module="com.springsource.org.eclipse.persistence" revision="1.1.0"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />

		<ivy:install settingsRef="settings" overwrite="true"
			organisation="org.eclipse.persistence" module="com.springsource.org.eclipse.persistence" revision="2.0.0"
			from="com.springsource.repository"
			to="my-repository"
			transitive="true" />
	</target>

	<!-- target: clean-cache -->
	<target name="clean-cache" depends="init-ivy" description="--> clean the cache">
		<ivy:cleancache settingsRef="settings" />
	</target>

	<!--  target: clean-repo  -->
	<target name="clean-repo" description="--> clean the destination repository">
		<delete dir="${dest.repo.dir}" failonerror="true" />
	</target>
</project>
~~~

Si dentro de la carpeta del repositorio ejecuto `ant -p` obtengo un listado de las tareas disponibles:

	$ ant -p

	Buildfile: build.xml

	Main targets:

	clean-cache              --> clean the cache
	clean-repo               --> clean the destination repository
	install-eclipselink      --> install eclipselink
	install-myfaces          --> install Apache MyFaces and dependecies
	install-spring           --> install Spring Framework and dependecies
	install-spring-batch     --> install Spring Batch and dependecies
	install-spring-security  --> install Spring Security and dependecies
	install-swf              --> install Spring Web Flow and dependecies
	install-trinidad         --> install Apache Trinidad and dependecies

Si ejecutamos algunas de las tareas, Ivy descarga las librerías y las copia en mi repositorio en la carpeta/home/miguel/repositorio-ivy/repository.

	$ ant install-spring

	Buildfile: build.xml

	init-ivy:

	install-spring:
	[ivy:install] :: Ivy 2.1.0 - 20090925235825 :: http://ant.apache.org/ivy/ ::
	[ivy:install] :: loading settings :: file = /home/miguel/repositorio-ivy/settings/ivysettings.xml
	[ivy:install] :: installing org.springframework#org.springframework.spring-library;2.5.6.A ::
	[ivy:install] :: resolving dependencies ::
	[ivy:install] found org.springframework#org.springframework.spring-library;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.aop;2.5.6.A in com.springsource.repository
	[ivy:install] found org.aopalliance#com.springsource.org.aopalliance;1.0.0 in com.springsource.repository
	[ivy:install] found org.apache.commons#com.springsource.org.apache.commons.logging;1.1.1 in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.beans;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.core;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.context;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.context.support;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.jdbc;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.transaction;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.jms;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.orm;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.web;2.5.6.A in com.springsource.repository
	[ivy:install] found org.springframework#org.springframework.web.servlet;2.5.6.A in com.springsource.repository
	[ivy:install] :: downloading artifacts to cache ::
	[ivy:install] :: installing in my-repository ::
	[ivy:install] published license to /home/miguel/repositorio-ivy/repository/org.springframework/org.springframework.spring-library/licenses/license-2.5.6.A.txt
	[ivy:install] published org.springframework.spring-library to /home/miguel/repositorio-ivy/repository/org.springframework/org.springframework.spring-library/librarys/org.springframework.spring-library-2.5.6.A.libd
	[ivy:install] published ivy to /home/miguel/repositorio-ivy/repository/org.springframework/org.springframework.spring-library/ivys/ivy-2.5.6.A.xml
	[ivy:install] published org.springframework.aop-sources to /home/miguel/repositorio-ivy/repository/org.springframework/org.springframework.aop/srcs/org.springframework.aop-sources-2.5.6.A.jar
	.
	.
	.
	.
	.
	[ivy:install] :: install resolution report ::
	[ivy:install] :: resolution report :: resolve 0ms :: artifacts dl 114ms
	-------------------------------------------------------------
	|           |                  modules      ||  artifacts   |
	|   conf    | number| search|dwnlded|evicted||number|dwnlded|
	-------------------------------------------------------------
	|  default  |  14   |   0   |   0   |   0   ||  41  |   0   |
	-------------------------------------------------------------

	BUILD SUCCESSFUL

	Total time: 3 seconds

Además Ivy crea una caché en la carpeta `/home/miguel/repositorio-ivy/cache.`

Ya tengo mi repositorio Ivy. Ahora sólo falta configurar algún proyecto Java para usarlo. La manera más fácil es usando [IvyDE,](http://ant.apache.org/ivy/ivyde/index.html) un plugin para Eclipse.
