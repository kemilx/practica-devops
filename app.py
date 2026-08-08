import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b'{"status":"ok"}'
            content_type = "application/json; charset=utf-8"
            status = 200
        elif self.path == "/":
            body = """<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hola Mundo - DevOps</title>
    <style>
      body { margin: 0; min-height: 100vh; display: grid; place-items: center;
             font-family: system-ui, sans-serif; color: #172554;
             background: linear-gradient(135deg, #dbeafe, #f8fafc); }
      main { padding: 3rem; text-align: center; background: #ffffffcc;
             border-radius: 1rem; box-shadow: 0 1rem 3rem #1e3a8a22; }
      h1 { margin: 0 0 .5rem; font-size: clamp(2.5rem, 8vw, 5rem); }
      p { margin: 0; color: #475569; }
    </style>
  </head>
  <body><main><h1>¡Hola, mundo! 👋</h1><p>Aplicación web ejecutándose con Docker.</p></main></body>
</html>""".encode("utf-8")
            content_type = "text/html; charset=utf-8"
            status = 200
        else:
            body = b"Not found"
            content_type = "text/plain; charset=utf-8"
            status = 404

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"Servidor disponible en http://0.0.0.0:{port}")
    ThreadingHTTPServer(("0.0.0.0", port), AppHandler).serve_forever()
