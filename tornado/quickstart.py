import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    print("1.creating the app")
    app = make_app()
    print("2.listening")
    app.listen(8888)
    print("3.starts loop")
    tornado.ioloop.IOLoop.current().start()
