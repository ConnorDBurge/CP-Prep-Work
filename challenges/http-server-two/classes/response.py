from jinja2 import Template


class Response:

    def __init__(self, route, variables=None):
        self.build_body(route, variables)
        self.response = self.build_response()

    def __str__(self):
        return self.response

    def encode(self):
        return self.response.encode()

    def build_body(self, route, variables):
        view = Template(self.get_template(route))
        body = view.render() if variables is None else view.render(**variables)
        self.body = body

    def build_response(self):
        return f"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\nContent-Length:{len(self.body)}\r\n\r\n{self.body}"

    def get_template(self, route):
        with open(f'./templates/{route}.html', 'r') as file:
            return file.read()
