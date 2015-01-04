---
template: post
title: "Apache Trinidad y Spring Web Flow"
date: 2012-02-13
tags:
 - Apache Trinidad
 - Spring Web Flow
---

**Actualización (08/12/2012):** Según la [documentación](http://static.springsource.org/spring-webflow/docs/2.3.0.RELEASE/spring-webflow-reference/htmlsingle/spring-webflow-reference.html#spring-faces-webflow-config-jsf2), y a partir de la versión 2.2.0 de Spring Web Flow, para usar JSF2 se configura el [JsfFlowHandlerAdapter](http://static.springsource.org/spring-webflow/docs/2.3.x/javadoc-api/org/springframework/faces/webflow/JsfFlowHandlerAdapter.html) que inicializa un [JsfAjaxHandler](http://static.springsource.org/spring-webflow/docs/2.3.x/javadoc-api/org/springframework/faces/webflow/JsfAjaxHandler.html), por lo que ya no necesitamos nuestro propio AjaxHandler.

-----

Para [integrar](http://static.springsource.org/spring-webflow/docs/2.3.x/spring-webflow-reference/html/ch13s13.html) Apache Trinidad con Spring Web Flow necesitamos un [AjaxHandler](http://jira.springsource.org/browse/SWF-1160)

Con la introducción de la versión de Apache Trinidad para JSF 2 hay que hacer algunas modificaciones ya que la identificación de las solicitudes ajax ha sido modificada.

<script src="https://gist.github.com/msosvi/1820713.js">
</script>
