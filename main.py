import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# インデックスページを表示します
# Googleにログインしてもらいます
CONTENT_TYPE = 'text/html; charset=utf-8'
INDEX_HTML = 'index.html'
class MainHandler(webapp.RequestHandler):
  def get(self):
    # 出力
    self.response.headers['Content-Type'] = CONTENT_TYPE
    path = os.path.join( os.path.dirname(__file__), INDEX_HTML )
    self.response.out.write( template.render(path, {}) )

# アクセス元の環境変数情報を表示します
RETURN_HTML = '<a href="/">戻る</a><br/><br/>'
class EnvHandler(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()

    # 未ログインなら、ログインページへリダイレクトして終了
    if not user:
      self.redirect(users.create_login_url(self.request.uri))
      return

    self.response.headers['Content-Type'] = CONTENT_TYPE
    self.response.out.write( RETURN_HTML )
    for k, v in os.environ.iteritems():
      self.response.out.write( k + ':' + v + "<br/>" )

# 指定システムの応答時間を表示します
class DisplayDesignHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = CONTENT_TYPE
    self.response.out.write( RETURN_HTML )
    self.response.out.write( '応答時間を表示する予定です…' )

# 指定システムの応答時間を計測します
class FetchDesignHandler(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = CONTENT_TYPE
    self.response.out.write( RETURN_HTML )
    self.response.out.write( '応答時間を計測しました！' )

# Twitterアーカイヴページへリダイレクトします
TWITTER_ARCHIVE_URL = 'http://ringio-twitter-archive.appspot.com/'
class TwitterArchiveHandler(webapp.RequestHandler):
  def get(self):
    self.redirect( TWITTER_ARCHIVE_URL )
    return

# Blogページへリダイレクトします
BLOG_URL = 'http://ringio-blog.appspot.com/'
class BlogHandler(webapp.RequestHandler):
  def get(self):
    self.redirect( BLOG_URL )
    return

# Twitterアーカイヴページへリダイレクトします
MEIGEN_URL = 'http://ringio-meigen.appspot.com/'
class MeigenHandler(webapp.RequestHandler):
  def get(self):
    self.redirect( MEIGEN_URL )
    return

# webapp フレームワークのURLマッピングです
application = webapp.WSGIApplication(
                                     [
                                     	('/', MainHandler),
                                     	('/env/', EnvHandler),
                                     	('/meigen/', MeigenHandler),
                                     	('/design/', DisplayDesignHandler),
                                     	('/fetch/design/', FetchDesignHandler),
                                     	('/twitter_archive/', TwitterArchiveHandler),
                                     	('/blog/', BlogHandler)
                                     ],
                                     debug=True)

# WebApp フレームワークのメインメソッドです
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()