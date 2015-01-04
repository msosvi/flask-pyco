---
template: post
title: "Recuperar Grub"
date: 2010-03-06
tags:
 - Shell
 - Grub
 - GNU/Linux
---

Siempre es bueno tener estos [pasos para recuperar Grub](http://www.ubuntu-es.org/?q=node/121309) arrancando con un Live CD:

1. Arrancar el equipo desde un cd o memoria usb de GNU/Linux (en mi caso Ubuntu 9.10.).
2. Abrir un terminal de comandos.
3. Buscar la partición de Linux que contenga la instalación de GNU/Linux, será algo como /dev/sda5. Con el siguiente comando vemos todas las particiones y buscamos la que tenga formato ext4 o linux.

		$ sudo fdisk -l

4. Montar la partición que contenga la instalación de GNU/Linux.

		$ sudo mount -t ext4 /dev/sda5 /mnt

5. Montar el directorio `/dev` en `/mnt/dev`, porque sino el sistema no encontrará luego las unidades a modificar/instalar el Grub2.

		$ sudo mount --bind /dev /mnt/dev

6. Decirle al sistema que `/mnt` va a ser la raiz.

		$ sudo chroot /mnt

7. Ahora reinstalamos Grub2 en el disco que nos interese, que en mi caso es sda.

		$ sudo grub-install /dev/sda

Sólo queda apagar y arrancar desde el disco duro, Grub debería estar en su sitio otra vez.
