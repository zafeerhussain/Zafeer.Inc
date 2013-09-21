#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2



from secret import Constants
from google.appengine.ext import db



template_dir = os.path.join(os.path.dirname(__file__), 'templates')

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)
      
            
class BaseHandler(webapp2.RequestHandler):
    """A Base Handler used to handle all requests"""
    user = None
    
    def write (self, *a, **kw):
        """ Write a response"""
        self.response.out.write(*a, **kw)
        
    def render_str (self, template, **params):
        """ Render a template with the passed params"""
        params['user'] = self.user;
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render (self, template, **kw):
        """ Render a template with the passed params"""
        self.write(self.render_str(template, **kw))

   
        
        
        

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()


class MainPage(BaseHandler):
    def get(self):
        self.render('base.html')

class Set(BaseHandler):
    def get(self):
        self.render('clock.html')

class Met(BaseHandler):
    def get(self):
        self.render('wiki.html')

class Ret(BaseHandler):
    def get(self):
        self.render('music.html')

class Get(BaseHandler):
    def get(self):
        self.render('googlefbdcbad0318f9b79.html')

class Det(BaseHandler):
    def get(self):
        self.render('video.html')


       
        
      

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/clock', Set),
                               ('/wiki', Met),
                               ('/music', Ret),
                               ('/googlefbdcbad0318f9b79.html', Get),
                               ('/video', Det),
	                           ], debug=True)
