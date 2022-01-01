from classes.router import Router
from classes.response import Response


@Router.route('/grid')
def index(request):
    response = Response('index')
    return response
