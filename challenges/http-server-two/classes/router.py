class Router:
    routes = []  # a class variable that will hold all of the routes on our application

    @classmethod
    def route(self, path, method='get'):
        def add_to_routes(function):
            route = {'path': path, 'function': function, 'method': method}
            self.routes.append(route)
        return add_to_routes

    @classmethod
    def process(self, request):
        parsed_request = request.attributes
        for route in self.routes:
            if route['path'] == parsed_request['Resource'] and route['method'].lower() == parsed_request['Method'].lower():
                return route['function']()
        return 'HTTP/1.1 404 Not Found \r\n'
