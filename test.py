# -*- coding:utf-8 -*-
# __author__='chenliclchen'

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response("200 ok", [("Content-Type", "text/html")])
    name = environ['PATH_INFO'][1:]
    return ["<h1>hello %s</h1>" % name]


http_server = make_server("", 880, application)
print "start server ......"
http_server.serve_forever()

# 使用http://127.0.0.1:880/ 打开