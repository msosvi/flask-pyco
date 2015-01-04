---
template: post
title: "Tamaño Máximo del Contenido de la Solicitud HTTP en Lotus Domino"
date: 2009-10-04
tags:
 - Lotus Domino
 - iNotes
---

Hace poco me encontré con que el envío de correos con un fichero anexo de 10 MiB o más, usando iNotes, falla, el navegador pierde la conexión con el servidor. Estos mismos correos usando el cliente Lotus Notes se envían sin problemas.
Compruebo, por desconfiado, la restricción del tamaño de los mensajes:

[![](http://dl.getdropbox.com/u/302696/blog_files/maximun_http_request/maximun_message_size.jpg)](http://dl.getdropbox.com/u/302696/blog_files/maximun_http_request/maximun_message_size.jpg)

Ya está claro que no es el problema.
En el documento del servidor, en la configuración del motor web, compruebo que las solicitudes POST tampoco están limitadas en tamaño:

[![](http://dl.getdropbox.com/u/302696/blog_files/maximun_http_request/maximum_post_data.jpg)](http://dl.getdropbox.com/u/302696/blog_files/maximun_http_request/maximum_post_data.jpg)

Pero todavía queda un parámetro por revisar (parámetros de configuración no faltan en un servidor Lotus Domino), los límites del protocolo HTTP en el documento del servidor:

[![](http://dl.getdropbox.com/u/302696/blog_files/maximun_http_request/maximun_http_request.jpg)](http://dl.getdropbox.com/u/302696/blog_files/maximun_http_request/maximun_http_request.jpg)

Aquí está el problema, aumentando o poniendo a cero este parámetro se soluciona.
