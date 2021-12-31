class Response:

    def __init__(self, body):
        self.attributes = dict()
        self.response = self.build_response(body)

    def build_response(self, body):
        html_body = f'<html><head><title>An Example Page</title></head><body>{body}</body></html>'

        return f"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\nContent-Length:{len(html_body)}\r\n\r\n{html_body}"

    def encode(self):
        return self.response.encode()
