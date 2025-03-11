from http.server import HTTPServer, SimpleHTTPRequestHandler

port = 8000
server_address = ('', port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print(f'http://localhost:{port}')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\nServer đã dừng.')
    httpd.server_close()