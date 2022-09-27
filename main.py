import http.server
http=http.server.HTTPServer(("",8000),
                            http.server.SimpleHTTPRequestHandler)

http.serve_forever()