---
template: post
title: Usando Rsync y Git para Hacer Copias de Seguridad.
date: 2009-12-12
tags:
 - Shell
 - Git
 - rsync
---

Podemos realizar copias de seguridad con histórico de forma sencilla usando [Rsync](http://www.samba.org/rsync/) para realizar la copia y [Git](http://git-scm.com/) para mantener el histórico.

Primero creamos el directorio de las copias y lo ponemos bajo el control de Git:

	$ mkdir backups
	$ cd backups
	$ git init

Ahora solo nos queda crear el script que se encarga de realizar la copia con rsync y añadir los cambios al histórico con git.

	#!/bin/sh

	backup_dir="/home/miguel/backups"
	rsync -av --delete /home/miguel/Documentos "$backup_dir"
	cd "$backup_dir"
	git add . -A
	git commit -m "Copia de seguridad. `date +%Y-%m-%d`"

Listo, cada vez que se realiza una nueva copia de la carpeta `Documentos`, los cambios se copian en la carpeta `backups` y se incorporan al repositorio de Git teniendo así una copia de seguridad con historia.
