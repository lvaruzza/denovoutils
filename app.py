from google.appengine.ext import webapp
import MainPage
import VelvetMem

from google.appengine.ext.webapp.util import run_wsgi_app


application = webapp.WSGIApplication([
          ('/', MainPage.MainPage),
          ('/velvetmem', VelvetMem.VelvetMem)
        ],debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
        
