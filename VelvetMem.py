import os
import math

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from appengine_utilities.sessions import Session
from google.appengine.ext import webapp

class VelvetMem(webapp.RequestHandler):
    values = {'mem': 0,
              'mem_gb':0,
              'cov':0,
              'readSize':50,
              'genomeSize':5,
              'k':23,
              'backurl':'/',
              'numReads': 200}

    form_path = os.path.join(os.path.dirname(__file__), 'velvetmem.html')
    session = Session()

    def get(self):
        self.session = Session()
        if (not self.session.has_key('values')):
            self.session['values']=self.values

        self.response.out.write(template.render(self.form_path, self.session['values']))

    def post(self):
        path = os.path.join(os.path.dirname(__file__), 'form.html')
        readSize = int(self.request.get('readSize'));
        genomeSize = int(self.request.get('genomeSize'));
        numReads = int(self.request.get('numReads'));
        k = int(self.request.get('k'));
        self.session = Session();

        mem = -109635 + 18977*readSize + 86326*genomeSize + 233353*numReads - 51092*k;
        self.session['values']['mem'] = mem;
        self.session['values']['mem_gb'] = int(math.ceil(mem/(1024.0*1024)));
        self.session['values']['cov'] = readSize*numReads*1.0/genomeSize;
        self.session['values']['readSize'] = readSize;
        self.session['values']['genomeSize'] = genomeSize;
        self.session['values']['numReads'] = numReads;
        self.session['values']['k'] = k;

        self.response.out.write(template.render(self.form_path, self.session['values']))
        
