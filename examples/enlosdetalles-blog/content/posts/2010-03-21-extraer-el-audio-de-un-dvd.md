---
template: post
title: "Extraer el audio de un DVD"
date: 2010-03-21
tags:
 - Shell
 - GNU/Linux
---

Pequeño 
[script para extraer el audio de un DVD](http://www.gs1.ubuntuforums.org/showpost.php?p=8452952&postcount=33). Después de alguna pequeña modificación queda así:

	#!/bin/bash

	# DVD Audio ripping script originally created		
	# by supertux from the Ubuntu forums:
	# http://ubuntuforums.org/showpost.php?p=4251034&amp;postcount=12
	# Modified by NTolerance to list DVD information,
	# accept command line arguments, and output 128kbit MP3 files.
	# Modified by strangeattractor to pad zeros in the file name
	# and to use tcaud instead of raw for exporting
	# Requires installation of transcode, lsdvd, and lame packages from the
	# Ubuntu repositories and probably other packages related to DVD
	# decryption and playback.
	# Modified by msosvi to add source argument
	# usage: dvd-audio-rip.sh [Source] [Title] [TotalTracks]
	# example: dvd-audio-rip.sh //media/cdrom0 04 06
	# Running without Title or TotalTracks arguments will
	# display DVD track information.

	case "$2" in 
		"") 
			echo "DVD Title and Track Information:"
			echo
			lsdvd -v $1 | grep 'Length:' | cut -d, -f1,2
			echo
			echo "usage: dvd-audio-rip.sh [Source] [Title] [TotalTracks]"
			echo "example: dvd-audio-rip.sh /media/cdrom0 04 06"
			exit $E_PARAM
		;;

		*) 

			export title=$2
			export totaltracks=$3

			export src=$1
			export tracks=1

			until [ $tracks -gt $totaltracks ]; do
				transcode -i $src -x dvd,dvd -T $title,$tracks,1 -a 0 -y null,tcaud -b 128 -m `printf "%02d" $title`-track-`printf "%03d" $tracks`.mp3
				let tracks+=1
			done
 		;;
	esac

El script necesita tres parámetros: Source, Title, TotalTracks. Si lo lanzamos sólo con el primero, la carpeta o dispositivo donde esté el DVD, muestra información del mismo. 

Un ejemplo, ejecutamos el script indicándole donde está el DVD para obtener la información del título y los capítulos a extraer:

	$ ./dvd-audio-rip.sh /media/cdrom0
	DVD Title and Track Information:

	libdvdread: Using libdvdcss version 1.2.5 for DVD access
	libdvdread: Attempting to use device /dev/sr0 mounted on /media/cdrom0 for CSS authentication
	Couldn't read enough bytes for title.
	Title: 01, Length: 00:58:52.320 Chapters: 13
	Title: 02, Length: 00:04:37.020 Chapters: 01
	Title: 03, Length: 00:04:23.010 Chapters: 01
	Title: 04, Length: 00:03:21.000 Chapters: 01
	Title: 05, Length: 00:04:57.210 Chapters: 01
	Title: 06, Length: 00:06:22.020 Chapters: 01
	Title: 07, Length: 00:05:31.200 Chapters: 01
	Title: 08, Length: 00:04:00.210 Chapters: 01
	Title: 09, Length: 00:06:42.000 Chapters: 01
	Title: 10, Length: 00:05:38.010 Chapters: 01
	Title: 11, Length: 00:03:58.020 Chapters: 01
	Title: 12, Length: 00:05:07.200 Chapters: 01
	Title: 13, Length: 00:03:44.010 Chapters: 01
	Title: 14, Length: 00:00:27.120 Chapters: 01
	Title: 15, Length: 00:00:05.140 Chapters: 01
	Title: 16, Length: 00:00:01.330 Chapters: 01
	Title: 17, Length: 00:00:26.000 Chapters: 01

	usage: dvd-audio-rip.sh [Source] [Title] [TotalTracks]
	example: dvd-audio-rip.sh /media/cdrom0 04 06

Y ahora lo lanzamos para extraer el audio de los 13 capítulos del primer título:

	$./dvd-audio-rip.sh /media/cdrom0 01 13
