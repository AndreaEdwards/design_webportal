#!/usr/bin/env python
import os
from os.path import dirname, join
from base64 import b64encode
from uuid import uuid4
#import pymol
import webbrowser
#from web import pymolhttpd
import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options, parse_command_line

from handlers.base_handlers import (
    IndexHandler
    )
from handlers.protein_handlers import (
    ProteinHandler
    )

class Application(tornado.web.Application):
    def __init__(self):
        DIRNAME = dirname(__file__)
        STATIC_PATH = join(DIRNAME, "static")
        TEMPLATE_PATH = join(DIRNAME, "templates")  # base folder for webpages
        RES_PATH = join(DIRNAME, "results")
        COOKIE_SECRET = b64encode(uuid4().bytes + uuid4().bytes)
        handlers = [
                (r"/", IndexHandler),
                (r"/results/(.*)", tornado.web.StaticFileHandler,
                 {"path": RES_PATH}),
                (r"/static/(.*)", tornado.web.StaticFileHandler,
                 {"path": STATIC_PATH}),
                (r"/protein/", ProteinHandler),
                (r"/fetch_sequence_information/", ProteinHandler)
                ]
        settings = {
            "template_path": TEMPLATE_PATH,
            "debug": True,
            "cookie_secret": COOKIE_SECRET,
            "login_url": "/",
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    #pymol.finish_launching()
    port = int(os.environ.get("PORT", 5050))
    root = os.getcwd() + "/templates"
    #httpd = pymolhttpd.PymolHttpd(port=8085, root=root)
    #httpd.start()
    parse_command_line()
    http_server = HTTPServer(Application())
    http_server.listen(port)
    print "Tornado started on port", port
    webbrowser.open("localhost:%d"%port)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
