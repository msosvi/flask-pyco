---
template: post
title: "Groovy y JPA"
date: 2009-08-30
tags:
 - Groovy
 - JPA
---

Estoy probando Groovy y quería ver como se lleva con JPA y sus anotaciones. La sintaxis simplificada de Groovy es interesante a la hora de crear los beans de entidad.

Este es mi JavaBean con sus anotaciones JPA:

	package com.mycompany.modelo;

	import java.io.Serializable;
	import javax.persistence.*;

	@Entity
	@Table(name="CENTROS")
	public class CENTRO implements Serializable {

		@Id
		@Column(name="CODCENTRO")
		private String codigo;

		@Column(name="NOMBRECENTRO")
		private String nombre;

		public String getCodigo() {
			return codigo;
		}

		public void setCodigo(String codigo) {
			this.codigo = codigo;
		}

		public String getNombre() {
			return nombre;
		}

	   	public void setNombre(String nombre) {
			this.nombre = nombre;
		}

		public String toString(){
			return this.getCodigo();
		}

	    	public String getNombreEntero(){
        			return this.getCodigo()+" - " + this.getNombre();
		}

		public boolean equals(Object that){
			if (!(that instanceof Centro)){
				return false;
			}else{
				return this.codigo.equals(((Centro)that).getCodigo());
			}
		}
	}

Y una vez modificado el GroovyBean queda así:

	package com.mycompany.modelo;
	import javax.persistence.*;

	@Entity
	@Table(name="CENTROS")

	class Centro implements Serializable{
		@Id
		@Column(name="CODCENTRO")
		String codigo;

		@Column(name="NOMBREOFICINA")
		String nombre;

    		String getNombreEntero(){
        			return "$codigo - $nombre"
 		}

		String toString(){
        			return codigo;
    		}

		boolean equals(Object that){
			if (!(that instanceof Centro)){
				return false;
        			}else{
            			return this.codigo==that.codigo
			}
		}
	}

En la clase de Groovy desaparecen lo setters y getters (en realidad si están, pero de eso se encarga Groovy), los atributos y métodos son public por defecto, uso GStrings que permiten construir strings con código embedido y el operador sobrecargado '=='.

La clase una vez compilada, no tiene ningún problema con JPA y la persistencia funciona perfectamente.

Groovy cada vez me convence más.

El siguiente paso es usar Groovy en algún DAO para explotar aún más los GString al crear sentencias JPQL.
