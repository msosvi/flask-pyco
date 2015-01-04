---
template: post
title: "Leyendo Propiedades del Sistema en Spring"
date: 2009-08-22
tags:
 - Spring
---

Necesitaba acceder a un fichero y quería que la ruta fuera relativa al directorio de instalación del Tomcat. La duda era como acceder la valor de `catalina.home` en el fichero de configuración de Spring.

La documentación de referencia de Spring cuenta lo siguiente:

>The `PropertyPlaceholderConfigurer` doesn't only look for properties in the Properties file you specify, but also checks against the Java System properties if it cannot find a property you are trying to use. This behavior can be customized by setting the `systemPropertiesMode` property of the configurer. It has three values, one to tell the configurer to always override, one to let it override and one to let it override only if the property cannot be found in the properties file specified.

Así que lo que necesitaba era configurar un `PropertyPlaceholderConfigurer` con la propiedad `systemPropertiesMode` con el valor `SYSTEM_PROPERTIES_MODE_OVERRIDE`. A partir de aquí ya tengo disponible las propiedades del sistema y la ubicación del Tomcat con solo incluir en la configuración `${catalina.home}`.

La configuración de Spring queda así:

~~~ xml
<bean class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">
	<property name="systemPropertiesMode">
		<util:constant
			static-field="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer.SYSTEM_PROPERTIES_MODE_OVERRIDE" />
	</property>
</bean>

<bean id="myBean" class="com.mycompany.MyBean">
	<property name="myFilePath" value="${catalina.home}\forlder\myfile.txt" />
</bean>
~~~
