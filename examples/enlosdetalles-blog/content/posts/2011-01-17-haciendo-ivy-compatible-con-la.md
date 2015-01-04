---
template: post
title: "Haciendo a Ivy compatible con las versiones OSGi."
date: 2011-01-17
tags:
 - Ivy
---

La estrategia de [Ivy](http://ant.apache.org/ivy/) que selecciona, en caso de conflicto, el módulo con la última versión, no es compatible con el sistema de versiones de OSGi. Esto hace, por ejemplo, que Ivy seleccione la versión 2.5.6 de spring-beans y no la versión superior 2.5.6.SEC02, como se aprecia en la siguiente captura de pantalla:

[![](http://dl.dropbox.com/u/302696/blog_files/ivy_bushel/conflicts_ivy.gif)](http://dl.dropbox.com/u/302696/blog_files/ivy_bushel/conflicts_ivy.gif)

Este [bug](https://issues.apache.org/jira/browse/IVY-1208) está pendiente de solución. Hasta que publiquen una nueva versión de Ivy compatible con OSGi, para resolver correctamente las dependencias uso la librería [Bushel](http://code.google.com/p/bushel/) que incluye la clase `OsgiLatestStrategy`. Para usar esta estrategia por defecto, modifico la configuración de Ivy:

~~~ xml
<ivysettings>
	<classpath file="lib/bushel-0.6.1.jar" />
	<typedef name="osgi-latest" classname="com.googlecode.bushel.ivy.OsgiLatestStrategy" />

	<latest-strategies>
		<osgi-latest name="osgi-latest-revision" />
	</latest-strategies>

	<settings defaultResolver="my-repository" defaultLatestStrategy="osgi-latest-revision" />

	 ....

</ivysettings>
~~~

Usando esta nueva configuración, el resultado de los conflictos es ahora correcto:

[![](http://dl.dropbox.com/u/302696/blog_files/ivy_bushel/conflicts_bushel.gif)](http://dl.dropbox.com/u/302696/blog_files/ivy_bushel/conflicts_bushel.gif)
