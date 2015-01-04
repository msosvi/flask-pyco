---
template: post
title: "Esquema por defecto en JPA"
date: 2011-02-20
tags:
 - JPA
---

Para configurar, al usar JPA, el esquema de la base de datos por defecto, utilizo el siguiente fichero orm.xml (object relational mapping XML file):

~~~ xml
<entity-mappings xmlns="http://java.sun.com/xml/ns/persistence/orm"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://java.sun.com/xml/ns/persistence/orm
			http://java.sun.com/xml/ns/persistence/orm_1_0.xsd"
		version="1.0">

	<persistence-unit-metadata>
		<persistence-unit-defaults>
			<schema>MYSCHEMA</schema>
		</persistence-unit-defaults>
	</persistence-unit-metadata>
	<sequence-generator name="IdentitySeq"
		sequence-name="MYSCHEMA.SEQ_GEN_IDENTITY" allocation-size="50" />
</entity-mappings>
~~~

Además de configurar el esquema, declaro el generador de secuencia usado para crear los identificadores de las entidades, indicando correctamente el esquema de la base de datos al que pertenece la secuencia (el esquema por defecto, JPA sólo lo usa para el acceso a las entidades).
