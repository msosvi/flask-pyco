---
template: post
title: "Spock y Eclipse"
date: 2012-08-08
tags:
 - Eclipse
 - Spock
---

Para que [Spock](http://spockframework.org/) quede bien configurado en Eclipse no hay que saltarse el siguiente paso de la [configuración](http://code.google.com/p/spock/wiki/GettingStarted#Eclipse):

>Enable the following option: Preferences->Groovy->Use monospace font for JUnit. This is important for Spock's condition output to be aligned correctly.

Sin habilitar esta opción las salidas de las condiciones de Spock no se ven muy bien:

[![](http://dl.dropbox.com/u/302696/blog_files/spock_eclipse/spock_before.png)](http://dl.dropbox.com/u/302696/blog_files/spock_eclipse/spock_before.png)

Así están mucho mejor:

[![](http://dl.dropbox.com/u/302696/blog_files/spock_eclipse/spock_after.png)](http://dl.dropbox.com/u/302696/blog_files/spock_eclipse/spock_after.png)
