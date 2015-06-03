# -*- coding: utf-8 -*-
import yaml
import re
import os
import mistune
from . import utils
from datetime import time,date,datetime
from flask import Markup,render_template_string


class FileContentError(Exception):
    pass


class Page:

    def __init__(self,site,filepath,filecontent):
        self.site = site
        self.filepath = filepath
        self.fileext = os.path.splitext(self.filepath)[1]

        self.unrendered_content = None
        self.data = {}

        self.url= self._get_url ()

        if (os.sep in filepath):
            self.category =  filepath.split (os.sep)[0]
        else:
            self.category = "."

        #Split the file content into content and front matter.
        m = re.match ('(?:^---\s*\n*)(?P<front_matter>[\s\S]*)(?:^---\n)(?P<content>[\s\S]*)',filecontent,re.MULTILINE)

        if m:
            try:
                self.data.update(self._load_front_matter(m.group('front_matter')))
            except Exception as exc:
                raise FileContentError("Invalid front matter in file '%s': \n\n%s" % (filepath,exc))

            self.unrendered_content = m.group('content')
        else:
            raise FileContentError("Invalid content in file '%s'" % filepath)


    def __getitem__(self, key):
        """Allows access to the page metadata by using the page instance"""
        return self.data[key]

    def __lt__(self,other):
        if (self.sort_key != None) and (other.sort_key != None):
            return self.sort_key<other.sort_key

        if (self.sort_key == None) and (other.sort_key != None):
            return True

        return False

    def is_markdown(self):
        """Returns true if the content page uses markdown"""
        return  self.fileext == self.site.config.markdown_ext


    def render_content(self,args={}):
        """Returns the rendered content of the page"""

        context = args.copy()
        context['site'] = self.site
        context['page'] = self

        rendered_content = render_template_string (self.unrendered_content,**context)

        if self.is_markdown():
            md = mistune.Markdown(renderer=self.site.mistune_renderer)
            rendered_content = md.render (rendered_content)

        return Markup(rendered_content)


    @property
    def template(self):
        if 'template' in self.data:
            if self.data['template'] == 'none':
                return None
            else:
                return self.data['template'] + '.html'
        else:
            return "default.html"


    @property
    def sort_key(self):
        if 'order_pages_by' in self.site.config:
            if self.site.config['order_pages_by'] in self.data:
                return self.data[self.site.config['order_pages_by']]
            else:
                return None
        else:
            return self.url


    @property
    def content(self):
        return self.render_content()


    @property
    def tags(self):
        """ Return the tags of page """
        if 'tags' in self.data:
            return self.data['tags']
        else:
            return []


    @property
    def next(self):
        index = self.site.pages.index(self)
        if index < len(self.site.pages)-1:
            return self.site.pages[index+1]
        else:
            return None


    @property
    def next_in_category(self):
        pages_in_category = self.site.categories[self.category]
        index = pages_in_category.index(self)
        if index < len(pages_in_category)-1:
            return pages_in_category[index+1]
        else:
            return None


    @property
    def previous(self):
        index = self.site.pages.index(self)
        if index > 0:
            return self.site.pages[index-1]
        else:
            return None


    @property
    def previous_in_category(self):
        pages_in_category = self.site.categories[self.category]
        index = pages_in_category.index(self)
        if index > 0:
            return pages_in_category[index-1]
        else:
            return None


    def _load_front_matter(self,front_matter):
        data = yaml.load(front_matter)

        #Convert all data keys to lower case
        data = {k.lower():v for k,v in data.items()}

        data['date'] = self._get_date(data)

        return data


    def _get_date(self,data):
        """ Returns de page date always as a datetime object
            because is needed to sort by date without
            the type error 'can't compare datetime.datetime to datetime.date'
        """

        if 'date' in data:
            if isinstance(data['date'], datetime):
                page_date = data['date']
            elif isinstance(data['date'], date):
                page_date = datetime.combine(data['date'], time.min)
            else:
                page_date = datetime.strptime(data['date'],self.site.config['date_format'])
        else:
            #To avoid errors when sorting by date all pages must be dated.
            page_date = datetime(1900,1,1)

        return page_date


    def _get_url(self):
        url = os.path.splitext(self.filepath)[0]

        head, tail = os.path.split(url)
        if tail == 'index': url = head

        url = utils.slugify(url)

        if self.fileext != self.site.config.markdown_ext and self.fileext != self.site.config.html_ext:
            url = url + self.fileext

        return url
