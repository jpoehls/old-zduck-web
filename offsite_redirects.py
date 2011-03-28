from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Photos(webapp.RequestHandler):
  def get(self):
    if "fishnpaws.com" in self.request.url:
      # Mom & Aunt Lorell's FRIENDS photostream
      self.redirect("http://www.flickr.com/gp/26412493@N07/7R425u")
    else:
      # Joshua & Kristina's FRIENDS photostream
      self.redirect("http://www.flickr.com/gp/25531422@N08/4p6S43")

class FamilyPhotos(webapp.RequestHandler):
  def get(self):
    if "fishnpaws.com" in self.request.url:
      # Mom & Aunt Lorell's FAMILY & FRIENDS photostream
      self.redirect("http://www.flickr.com/gp/26412493@N07/u86x6e")
    else:
      # Joshua & Kristina's FAMILY & FRIENDS photostream
      self.redirect("http://www.flickr.com/gp/25531422@N08/2AZM06")

class House(webapp.RequestHandler):
  def get(self):
    self.redirect("http://zduck.com/house")

application = webapp.WSGIApplication(
                                     [('/photos', Photos),
                                      ('/familyphotos', FamilyPhotos),
                                      ('/house', House)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
