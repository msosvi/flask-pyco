---
template: post
title: "The Tomcat JDBC Connection Pool"
date: 2011-02-26
tags:
 - Tomcat
---

[The Tomcat JDBC Connection Pool](http://people.apache.org/%7Efhanik/jdbc-pool/jdbc-pool.html) es una alternativa a la agrupación de conexiones de bases de datos Jakarta Commons ([commons-dbcp](http://commons.apache.org/dbcp/)).

Vamos ver los pasos necesarios para configurar en Tomcat un origen de datos con esta agrupación de conexiones:

* Añado el fichero del JDBC Connection Pool (está disponible
[en el repositorio de Spring](http://ebr.springsource.com/repository/app/bundle/detail?name=com.springsource.org.apache.tomcat.jdbc)) y del controlador de la base de datos en el directorio
`%CATALINA%/lib` del Tomcat.

* Configuro el origen datos como un recurso global en el `server.xml`, el atributo `factory` debe tener el valor `org.apache.tomcat.jdbc.pool.DataSourceFactory`:

~~~ xml
<GlobalNamingResources>
 	<Resource name="jdbc/dataSource" auth="Container"
 		factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
		type="javax.sql.DataSource"
		driverClassName="oracle.jdbc.driver.OracleDriver"
		url="jdbc:oracle:thin:@127.0.0.1:1521:mysid"
		username="scott" password="tiger"
		initialSize="2"
		maxActive="10"
		maxIdle="5"
		minIdle="5"
		maxWait="10000" />
</GlobalNamingResources>
~~~

* Para poder usar la fuente de datos, añado la etiqueta `<ResourceLink>` al contexto de la aplicación, en el archivo `META-INF/contex.xml`:

~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Context>
<Context>
 	<ResourceLink name="jdbc/dataSource" global="jdbc/dataSource" type="javax.sql.DataSource" />
</Context>
~~~
