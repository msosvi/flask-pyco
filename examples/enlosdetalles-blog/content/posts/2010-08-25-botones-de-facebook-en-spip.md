---
template: post
title: "Botones de Facebook en Spip"
date: 2010-08-25
tags:
 - Facebook
 - Spip
---

Para añadir el botón de Facebook para [recomendar](http://developers.facebook.com/docs/reference/plugins/like) o [compartir](http://developers.facebook.com/docs/share) un artículo en [Spip](http://www.spip.net/es) sólo hay que añadir el siguiente código al archivo `article.html` del esqueleto. Uso las balizas `#URL_SITE_SPIP` y `#URL_ARTICLE` para construir la dirección a compartir.

**Botón Recomendar**

[![](http://dl.dropbox.com/u/302696/blog_files/spip_facebook/likebutton.jpg)](http://dl.dropbox.com/u/302696/blog_files/spip_facebook/likebutton.jpg)

~~~ xml
<iframe allowtransparency="true" frameborder="0" scrolling="no"
    src="http://www.facebook.com/plugins
   /like.php?href=#URL_SITE_SPIP#URL_ARTICLE%2Fpage%2Fto%2Flike&
   layout=standard&
   show_faces=true&
   width=450&
   action=recommend&
   colorscheme=light&
   height=80"
   style="border: medium none; height: 80px; overflow: hidden; width: 450px;">
</iframe>
~~~


**Botón Compartir**

[![](http://dl.dropbox.com/u/302696/blog_files/spip_facebook/sharebutton.jpg)](http://dl.dropbox.com/u/302696/blog_files/spip_facebook/sharebutton.jpg)

~~~ xml
<a name="fb_share" type="button_count"
share_url="#URL_SITE_SPIP/#URL_ARTICLE">Compartir</a>
<script src="http://static.ak.fbcdn.net/connect.php/js/FB.Share"
        type="text/javascript">
</script>
~~~
