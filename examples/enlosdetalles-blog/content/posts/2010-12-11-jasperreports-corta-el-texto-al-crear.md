---
template: post
title: "JasperReports corta el texto al crear informes en formato Excel"
date: 2010-12-11
tags:
 - JasperReports
---

Al crear un informe en formato Excel usando [JaserReports](http://jasperforge.org/projects/jasperreports) el texto de las celdas se corta, si no tiene suficiente espacio.

A partir de la versión 2.0.3 se puede cambiar este comportamiento usando la propiedad `net.sf.jasperreports.print.keep.full.text`. Sólo tenemos que asignarle el valor true en el fichero jrxml del infome:


	<jasperReport ... >
		<property name="net.sf.jasperreports.print.keep.full.text" value="true" />
	 ...


**Recursos:**

* [JasperReports 2.0.3: (xls) long text is truncated ](http://www.jasperforge.org/plugins/espforum/view.php?group_id=102&forumid=103&topicid=35245) 
