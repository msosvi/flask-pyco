# -*- coding: utf-8 -*-
import os
import codecs
import logging
from operator import attrgetter
from flask import request,render_template, Markup,make_response,url_for
import mimetypes

from .page import Page, FileContentError
from .config import Config

class Site:

    def __init__(self,app=None,config_filename=None,mistune_renderer = None):

        mimetypes.init()
        self._create_logger(app)
        self._load_config(app,config_filename)

        self.mistune_renderer = mistune_renderer

        if self.config.development:
            self.logger.setLevel(logging.DEBUG)

        if app is not None:
            self.init_app(app)

        self.find_all_pages()


    def __getitem__(self, key):
        """Allows access to the public configuration by using the site instance """
        return self.config['site'][key]


    def init_app(self,app):
        app.add_url_rule('/', defaults={'path': ''}, view_func=self._catch_all)
        app.add_url_rule('/<path:path>/',view_func=self._catch_all)


    def find_all_pages(self):

        self.pages = []
        self.urls = {}
        self.errors = {}
        self.tags = {}
        self.categories = {}

        contentdir= os.path.join (self.root_path,self.config.contentdir)

        for root, subFolders, files in os.walk(contentdir):

            for filename in files:
                filepath = os.path.join(root, filename)

                with codecs.open( filepath, 'r','utf-8' ) as f:
                    relpath = os.path.relpath (filepath,contentdir)

                    try:
                        page = Page(self,relpath,f.read())
                    except FileContentError as e:
                        self.logger.error(" - Page not created: %s " % e.args[0])
                        continue

                if filename[0] == '_':
                    self.errors[os.path.splitext (filename[1:])[0]] = page
                else:
                    self.urls[page.url] = page
                    self.pages.append(page)

                    for tag in page.tags:
                        if tag not in self.tags:
                            self.tags[tag] = []

                        self.tags[tag].append(page)

                    if page.category not in self.categories:
                        self.categories[page.category] = []

                    self.categories[page.category].append(page)


        #Sort all pages.
        self.pages.sort(reverse=self.config.reverse_order)

        #Sort pages with the same tag.
        for tag in self.tags:
            self.tags[tag].sort(reverse=self.config.reverse_order)

        #Sort pages into categories.
        for category in self.categories:
            self.categories[category].sort(reverse=self.config.reverse_order)

        self.logger.info(" * Load site with %s pages and %s error pages from %s" % (len(self.pages),len(self.errors), contentdir))


    def url_for_theme (self,filename):
        """Returns the url for a static file into the theme folder"""
        return url_for ('static',filename="themes/%s/%s" % (self.config.theme,filename))


    def _create_logger (self,app):
        if app is not None:
            self.logger = app.logger
        else:
            self.logger = logging.getLogger('pyco')
            self.logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            self.logger.addHandler(handler)


    def _load_config (self,app,filename):
        self.root_path=""
        if app is not None:
            self.root_path = app.root_path

        if filename is None:
            self.config_filename = os.path.join (self.root_path,'config.yml')
            default_exits = os.path.exists(self.config_filename)
        else:
            self.config_filename = os.path.join (self.root_path,filename)

        self.config = Config()

        if (filename is None and default_exits) or filename is not None:
            self.config.from_ymal(self.config_filename)
            self.logger.info (" * Load configuration from %s" % self.config_filename)


    def _catch_all(self,path):
        if self.config.development:
            self.logger.debug (" * Development mode: reload site")
            self.find_all_pages()

        if path in self.urls:
            current_page = self.urls[path]
            args = request.args.to_dict(flat = False)
            return self._make_page_response(current_page,args)
        else:
            return self._error_404()

    def _make_page_response(self,page,args = {}):
        context = {'site' : self,
                   'page' : page,
                   'theme_dir' : 'themes/' + self.config.theme  }

        page_content = page.render_content(args)
        context['content'] = Markup(page_content)

        if page.template == None:
            resp = make_response (page_content)
            resp.mimetype = mimetypes.types_map[page.fileext]
        else:
            resp = make_response (render_template ("themes/%s/%s" % (self.config.theme,page.template), **context))
        return resp


    def _error_404(self):
        if '404' in self.errors:
            page_404 = self.errors['404']
            resp = self._make_page_response(page_404)
            return resp, 404

        else:
            return make_response ("Upps, no encuentro esa página"), 404
