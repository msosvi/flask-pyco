---
template: post
title: "Lotus Domino y Spring Security - Single Sign On (SSO)"
date: 2009-08-15
tags:
 - Lotus Domino
 - Spring
---

**Introducción.**

En este pequeño artículo voy a intentar explicar como extender Spring Security para lograr que una aplicación web participe en el SSO (Single Sign-on) junto con servidores Lotus Domino.

Para llegar a esta integración uso las ideas (y algo de código) presentadas en el artículo
[Lotus Domino and Apache Tomcat - Single Sign On (SSO)](http://www.automatedlogic.com/domblog.nsf/dx/DominoTomcatSSOIntegration), pero sustituyendo la configuración del servidor Tomcat y el `DominoLoginFilter` por el uso de Spring Security.

La aplicación web, usando Spring Security, comprueba si existe la cookie con el token LTPA,  si existe lo usa para conectarse al servidor Lotus Domino mediante DIIOP, autenticar al usuario y recuperar sus datos.

**SSO de Lotus Domino.**

Lotus Domino usa autenticación basada en cookie, mediante
**LTPA** ([Lightweight Third-Party Authentication](http://en.wikipedia.org/wiki/IBM_Lightweight_Third-Party_Authentication)). Cuando el usuario se autentica en un servidor Lotus Domino, proporcionando su nombre y contraseña, su navegador recibe una cookie de sesión que contiene el token LTPA.

Si el usuario, después de recibir esta cookie, accede a otro servidor que es miembro de la misma configuración de SSO que el primer servidor, el usuario será automáticamente autenticado sin necesidad de introducir su usuario y contraseña.

Hay que tener el cuenta que la autenticación basada en cookie requiere que todos los servidores que participen en el entorno de SSO sean accesibles desde un mismo dominio (por ejemplo lotusdomino.mycompany.com y appserver.mycompany.com) para que la cookie con el token LTPA sea visible por todos los servidores.

**Extensión y Configuración de Spring Security.**

El entorno descrito encaja en lo que Spring denomina "[Pre-Authentication Scenarios](http://static.springsource.org/spring-security/site/docs/2.0.x/reference/preauth.html)", en los que queremos usar Spring Securty para controlar las autorizaciones de nuestra aplicación, pero el usuario ya ha sido autenticado por algún sistema externo antes del acceso a la aplicación.

Usaremos las siguientes clases:

* [LotusDominoPreAuthenticatedProcessingFilter](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoPreAuthenticatedProcessingFilter.java)

* [LotusDominoUserDetailsService](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoUserDetailsService.java)

* [LotusDominoAuthenticationEntryPoint](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoAuthenticationEntryPoint.java)

* [LotusDominoUtil](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoUserDetailsService.java)

* [EmployeeDetails](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/EmployeeDetails.java)

Para configurar Spring Security usamos el fichero [security-config.xml](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/security-config.xml)

Vamos a introducir brevemente cada clase, indicando las clases o interfaces de Spring Security usadas y su cometido.

**[LotusDominoPreAuthenticatedProcessingFilter.](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoPreAuthenticatedProcessingFilter.java)**

Esta clase extiende el `AbstractPreAuthenticatedProcessingFilter` y se encarga de recuperar el LTPA token de la petición HTTP, y almacenarlo en la credenciales del objeto `Auhentication` usando el método `getPreAuthenticatedCredentials`.

**[LotusDominoUserDetailsService.](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoUserDetailsService.java)**

Implementa la interfaz `AuthenticationUserDetailsService`. El método principal de esta clase es `loadUserDetails` mediante el que crea un objeto `EmployeeDetails` con todos los datos del usuario autenticado que necesita la aplicación.

El método `loadUserDetails` recupera el LtpaToken, almacenado en las credenciales del objeto `Authentication` por el  `LotusDominoPreAuthenticatedProcessingFilter`, y lo usa para conectarse al servidor Lotus Domino mediante DIIOP y recuperar el nombre del usuario y los grupos a los que pertenece.Por último recupera los permisos asignado al usuario o a sus grupos en la aplicación. Estos permisos están recogidos en el fichero de configuración de Spring Security usando un `MapBasedAttributes2GrantedAuthoritiesMapper`.

**[LotusDominoAuthenticationEntryPoint.](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoAuthenticationEntryPoint.java)**

Implementa la interfaz `AuthenticationEntryPoint`. Esta clase se encarga de realizar la redirección al formulario de acceso de Lotus Domino en caso de intentar entrar a la aplicación sin una autenticación previa en el servidor Lotus Domino.  
Usamos el parámetro `RedirectTo` del acceso de Lotus Domino, para que una vez el usuario sea validado por el servidor Lotus Domino se dirija nuevamente a la aplicación.

**[LotusDominoUtil.](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/LotusDominoUtil.java)**

Clase de utilidad para gestionar las conexiones DIIOP al servidor Lotus Domino y recuperar la cookie LtpaToken (el [`HttpServletRequest.getCookies()`](http://www.163jsp.com/help/javaee50api/javax/servlet/http/HttpServletRequest.html#getCookies%28%29) me dió algunos problemas).

**[EmployeeDetails.](http://dl.getdropbox.com/u/302696/blog_files/springsecurity_lotusdomino/EmployeeDetails.java)**

Implementa la interfaz `UserDetails`. Almacena información del usuario autenticado recuperada por el  `UserDetailsService` y usada por la aplicación.

**Enlaces de Interés:**

* [Lotus Domino and Apache Tomcat - Single Sign On (SSO).](http://www.automatedlogic.com/domblog.nsf/dx/DominoTomcatSSOIntegration)

* [IBM Lightweight Third-Party Authentication.](http://en.wikipedia.org/wiki/IBM_Lightweight_Third-Party_Authentication)

* [Guide to configuring Single Sign-on (SSO).](http://www-01.ibm.com/support/docview.wss?uid=swg21217754)
