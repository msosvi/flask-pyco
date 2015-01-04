---
template: post
title: "Logging en EclipseLink usando SLF4J"
date: 2011-10-30
tags:
 - SLF4J
 - EclipseLink
---

[EclipseLink](http://www.eclipse.org/eclipselink/), la implementación de referencia de JPA, usa sus propias clases para realizar el registro de trazas (logging). EclipseLink se puede extender para usar otras librerías de logging como Apache Commons Logging o SLF4j. Para conseguirlo debemos crear nuestra propia implementación de [`SessionLog`](http://www.eclipse.org/eclipselink/api/2.0/org/eclipse/persistence/logging/SessionLog.html) y configurar EclipseLink para que la use con el parámetro `eclipselink.logging.logger`

Existen algunas implemetaciones de `SessionLog` para
[Apache Commons Logging](http://wiki.eclipse.org/EclipseLink/Foundation/Logging) y
[SLF4J](https://bugs.eclipse.org/bugs/show_bug.cgi?id=296391) pero con algunas carencias (la implementación para JCL hace referencia directa a la API de Log4j y la de SLF4J no permite el uso de las propiedades de EclipseLink para controlar el formato de los logs), por lo que he creado una implementación que usa SLF4j.


<script src="https://gist.github.com/1325764.js">
</script>
