import os

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from appengine_utilities.sessions import Session
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
    path = os.path.join(os.path.dirname(__file__), 'index.html')

    def get(self):
        self.response.out.write(template.render(self.path, {}))
        
