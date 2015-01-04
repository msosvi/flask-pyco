---
template: post
title: "Herencia en Spring Framework"
date: 2010-03-27
tags:
 - Spring
---


Siguiendo el principio  [DRY (Don't Repeart Yourself)](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself) vamos a reutilizar una declaración de un bean usando la [herencia en Spring](http://static.springsource.org/spring/docs/2.5.x/reference/beans.html#beans-child-bean-definitions).

Tenemos un bean de un servicio de acceso a datos, que necesita muchos DAOS y parámetros.

~~~ xml
<bean id="service" class="net.enlosdetalles.services.JpaService" scope="session">
	<!-- Daos -->
	 <property name="personDao">
		 <bean class="net.enlosdetalles.services.daos.PersonJpaDao" />
	 </property>

	 <property name="searchDao">
		 <bean class="net.enlosdetalles.services.search.SearchJpaDao" />
	 </property>

	 <!-- Parámetros de configuración -->
	 <property name="percent" value="0.1" />
</bean>
~~~

Este servicio es usado por una aplicación Web por lo que el `scope` está inicializado a `session`. Si queremos usar este servicio en otro sitio, por ejemplo en trabajos lanzados por [Quartz](http://quartz-scheduler.org/), necesitamos que el `scope` no sea de `session` sino `prototype`. Podemos estar tentados de repetir toda la definición del bean cambiando el `id` y el `scope` . No lo hagas, no hace falta y te arrepentirás. Mejor usar la herencia de Spring. Definimos el bean como `abstracto` y creamos las definiciones de los servicios, cada uno con su `scope` e `id`, usando el atributo `parent` para definir la herencia:

~~~ xml
<bean id="abstractService" abstract="true" class="net.enlosdetalles.services.JpaService">
	<!-- Daos -->
	 <property name="personDao">
		 <bean class="net.enlosdetalles.services.daos.PersonJpaDao" />
	 </property>

	 <property name="searchDao">
		 <bean class="net.enlosdetalles.services.search.SearchJpaDao" />
	 </property>

	 <!-- Parámetros de configuración -->
	 <property name="percent" value="0.1" />
</bean>

<bean id="service" parent="abstractService" scope="session" />

<bean id="batchService" parent="abstractService" scope="prototype" />
~~~
