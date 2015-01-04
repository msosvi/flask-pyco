---
template: post
title: "Como recuperar el MBR de Windows con GNU/Linux"
date: 2010-03-06
tags:
 - GNU/Linux
 - Windows
---

Hay varias maneras de recuperar el MBR de Windows con un Live CD de GNU/Linux, esta es una de ellas:

	$ sudo apt-get install syslinux
	$ sudo dd if=/usr/lib/syslinux/mbr.bin of=/dev/sda
