import os, functools, http.server, socketserver

DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
with socketserver.TCPServer(("127.0.0.1", 4178), Handler) as httpd:
    httpd.serve_forever()
