---
template: post
title: "Último día del mes con Joda"
date: 2010-11-26
tags:
 - Java
---

Con [Joda-Time](http://joda-time.sourceforge.net/index.html) es muy fácil obtener la fecha fin de mes a partir de otra fecha:

~~~ java
import org.joda.time.DateTime;
...

DateTime fecha=new DataTime();
DateTime fechaFinMes=fecha.dayOfMonth().withMaximumValue();
~~~


**Recursos:**

* [Tutorial de JodaTime en developerWorks.](http://www.ibm.com/developerworks/java/library/j-jodatime.html)
