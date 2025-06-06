from http.server import SimpleHTTPRequestHandler, HTTPServer

def generate_html():
    content = ""
    content += "<!DOCTYPE html>\n"
    content += "<html>\n<head>\n"
    content += "<title>Diya's Delight Restaurant</title>\n"
    content += "<style>\n"
    content += "body { font-family: Arial; margin: 0; background-color: #f8f0e3; }\n"
    content += "header { background-color: #e07a5f; padding: 20px; color: white; text-align: center; }\n"
    content += "nav { background-color: #f4a261; padding: 10px; text-align: center; }\n"
    content += "nav a { margin: 10px; text-decoration: none; color: white; font-weight: bold; }\n"
    content += "section { padding: 20px; }\n"
    content += "footer { background-color: #264653; color: white; text-align: center; padding: 10px; position: fixed; width: 100%; bottom: 0; }\n"
    content += "</style>\n</head>\n<body>\n"
    content += "<header>\n<h1>Welcome to Diya's Delight</h1>\n"
    content += "<p>Your cozy corner for delicious food</p>\n</header>\n"
    content += "<nav>\n"
    content += '<a href="#">Home</a>\n'
    content += '<a href="#">Menu</a>\n'
    content += '<a href="#">About</a>\n'
    content += '<a href="#">Contact</a>\n'
    content += "</nav>\n"
    content += "<section>\n<h2>Today's Special</h2>\n"
    content += "<p>Paneer Butter Masala with Garlic Naan - ₹250</p>\n"
    content += "<p>Masala Dosa with Coconut Chutney - ₹120</p>\n"
    content += "</section>\n"
    content += "<footer>\n<p>&copy; 2025 Diya's Delight. All rights reserved.</p>\n</footer>\n"
    content += "</body>\n</html>"
    return content

class RestaurantHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            html_content = generate_html()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        else:
            self.send_error(404, "Page Not Found")

if __name__ == "__main__":
    port = 8000
    print(f"Serving on http://localhost:{port}")
    server_address = ("", port)
    httpd = HTTPServer(server_address, RestaurantHandler)
    httpd.serve_forever()
