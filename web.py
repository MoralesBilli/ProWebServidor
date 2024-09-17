from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

contenido = {
     '/proyecto/1': """<html>
             <h1>Proyecto: 1</h1>
             <head>
             <meta charset="UTF-8" />
             <meta name="viewport" content="width=device-width, initial-scale=1" />
             <title>Programacion web</title>
              <link href="css/style.css" rel="stylesheet" />
             </head>
             <p>Nombre: Billi Joel.</p>
              </html>""",
     '/proyecto/2': """<html>
             <h1>Proyecto: 2</h1>
             <p>Segunda pagina almacenada \t Numero de control: 21212002 </p>
             <p>Cambio realizado en cloud9</p>
             <p>Cambio realizado en cloud9</p>
             </html>""",
     '/proyecto/3': """<html>
             <h1>Proyecto: 3</h1>
             <p>Tercer contenido almacenado \t Carrera: Ingenieria en sistemas computacionales</p>
             </html>"""}

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.path == "/":
            conten = self.get_response()
        else:
            conten = contenido.get(self.path, None)

        if conten:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(conten.encode("utf-8"))
            
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>Página no encontrada</h1>".encode("utf-8"))
            

    def get_response(self):
        try:
            
            with open('home.html') as file:
                return file.read()
        except Exception as e:
                return f"<h1>Error al cargar la página: {e}</h1>"
        
    
if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()

