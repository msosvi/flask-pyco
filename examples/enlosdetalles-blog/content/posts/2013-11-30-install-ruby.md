---
template: post
title: "Instalando Ruby y Jekyll"
date: 2013-11-30
tags:
 - GNU/Linux
 - Ruby
 - Jekyll
---

Vamos a instalar Ruby y [Jekyll](http://jekyllrb.com/) en Ubuntu usando [Ruby Version Manager (RVM)](https://rvm.io/).

Lo primero es instalar RVM. La url [get.rvm.io](http://get.rvm.io) redirige al script de instalación que está en <https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer>.

	$ sudo apt-get update
	$ sudo apt-get install curl
	$ curl -L get.rvm.io | bash -s stable

      % Total    % Received % Xferd  Average Speed   Time    Time           Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   184  100   184    0     0    268      0 --:--:-- --:--:-- --:--:--   542
    100 19549  100 19549    0     0   6814      0  0:00:02  0:00:02 --:--:-- 18961
    Downloading https://github.com/wayneeseguin/rvm/archive/stable.tar.gz

    Installing RVM to /home/miguel/.rvm/
        Adding rvm PATH line to /home/miguel/.bashrc /home/miguel/.zshrc.
        Adding rvm loading line to /home/miguel/.bash_profile /home/miguel/.zlogin.
    Installation of RVM in /home/miguel/.rvm/ is almost complete:

      * To start using RVM you need to run `source /home/miguel/.rvm/scripts/rvm`
        in all your open shell windows, in rare cases you need to reopen all shell windows.

    # Miguel,
    #
    #   Thank you for using RVM!
    #   We sincerely hope that RVM helps to make your life easier and more enjoyable!!!
    #
    # ~Wayne, Michal & team.

    In case of problems: http://rvm.io/help and https://twitter.com/rvm_io


Para no tener que ejecutar `source ~/.rvm/scripts/rvm` cada vez que usamos RVM o Ruby hay que seguir los pasos indicados en [Integrating RVM with gnome-terminal](https://rvm.io/integration/gnome-terminal/) y marcar el checkbox '*Run command as login shell*' en la pestaña
'*Title and Command*' dentro de Preferencias del perfil del Terminal de Gnome (pestaña '*Título y comando*' y checkbox '*Ejecutar el comando como un intérprete de conexión*' si tienes la traducción al español de Ubuntu). Para entender bien lo que estamos haciendo podemos leer [What shell login means ('bash -l')](https://rvm.io/support/faq#what-shell-login-means-bash-l).

Una vez hecho esto al ejecutar `type rvm | head -n 1` debemos leer el mensaje `rvm: es una función`.

Ya tengo instalado RVM, lo compruebo con:

    $ rvm --version
    rvm 1.24.6 (stable) by Wayne E. Seguin <wayneeseguin@gmail.com>, Michal Papis <mpapis@gmail.com> [https://rvm.io/]

Para comprobar si tengo instalados todos los paquetes necesarios en mi Ubuntu ejecuto:

	$ rvm requirements

Ahora instalo Ruby y compruebo que funciona.

    $ rvm install 2.0.0
    $ ruby -v
    ruby 2.0.0p353 (2013-11-22 revision 43784) [x86_64-linux]

Instalo RubyGems y por último Jekyll

	$ rvm rubygems current
	$ gem install jekyll

Listo para ejecutar mi blog con Jekyll

    $ cd enlosdetalles-blog
    $ jekyll serve -w
    Configuration file: /home/miguel/enlosdetalles-blog/_config.yml
                Source: /home/miguel/enlosdetalles-blog
           Destination: /home/miguel/enlosdetalles-blog/_site
          Generating... done.
     Auto-regeneration: enabled
        Server address: http://0.0.0.0:4000
      Server running... press ctrl-c to stop.
