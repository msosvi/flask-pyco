---
template: post
title: "Llamando subflows con Spring Web Flow"
date: 2010-06-10
tags:
 - Spring Web Flow
 - Spring
---

Spring Web Flow permite hacer llamadas a subflows pasando valores de entrada y recuperando valores de salida. Veamos como.

En la configuración del flujo llamador usamos el elemento input para pasar valores al subflow, en el ejemplo  (muestro sólo la parte de la configuración del subflow) pasamos las variables `cliente` y  `readOnly` que se añadirán al flowScope del flujo llamado.

~~~ xml
<subflow-state id="edicionNuevoCliente" subflow="edicionCliente">
	<input name="cliente" />
	<input name="readOnly" value="false" />

	<transition on="VOLVER" to="listadoClientes">
		<set name="flowScope.cliente" value="currentEvent.attributes.cliente"/>
	</transition>
</subflow-state>
~~~

En el log vemos la llamada al subflow y como Spring Web Flow asigna los valores a los input:

	13:19:15,179 DEBUG FlowActionListener:85 - Event 'MOSTRAR_NUEVO_CLIENTE' detected
	13:19:45,632 DEBUG Transition:213 - Executing [Transition@325aa1 on = MOSTRAR_NUEVO_CLIENTE, to = edicionNuevoCliente]
	13:21:17,101 DEBUG SubflowState:99 - Calling subflow 'edicionCliente' with input map['readOnly' -> false, 'cliente' -> com.mycompany.modelo.Cliente@9685fb]


En la configuración del flujo llamado declaramos las variables de entrada como requeridas y en el estado final retornamos al flujo llamador el objeto `cliente` usando el elemento `output`:

~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<flow xmlns="http://www.springframework.org/schema/webflow"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/webflow http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">

	<input name="cliente" required="true" />
	<input name="readOnly" required="true" />

	<view-state id="edicionCliente" view="edicionCliente.jspx">
		<var name="clienteController" class="com.mycompamy.backing.ClienteController" />

		<transition on="TERMINAR" to="VOLVER" />
	</view-state>

	<end-state id="VOLVER" >
		<output name="cliente" />
	</end-state>
</flow>
~~~

La recuperación del objeto `cliente` devuelto, en el flujo llamador, la hacemos añadiendo una transición. En el ejemplo añadimos al `flowScope` del flujo llamador el objeto `cliente` retornado por el subflow:

~~~ xml
<transition on="VOLVER" to="listadoClientes">
	<set name="flowScope.cliente" value="currentEvent.attributes.cliente"/>
</transition>
~~~

Recuperar el objeto a la salida sólo es necesario si en el subflow borramos o sustituimos el objeto cliente. Si sólo realizamos modificaciones en el estado del objeto no hace falta, porque el mismo objeto cliente está en el flowScope del flujo llamador y en el flowScope del flujo llamado o subflow.
