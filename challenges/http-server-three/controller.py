from classes.router import Router
from classes.response import Response
from classes.facts import Fact
import datetime


@Router.route('/')
def index(request):
    response = Response('index', {'phrase': 'Hello World'})
    return response


@Router.route('/time')
def time(request):
    response = Response('time', {'time': datetime.datetime.now()})
    return response


@Router.route('/facts')
def facts(request):
    response = Response('all_facts', {'facts': Fact.all_facts()})
    return response
