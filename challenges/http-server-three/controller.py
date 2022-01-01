from classes.router import Router
from classes.response import Response
from classes.facts import Fact
import datetime
import re
import csv


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


@Router.route(r'\/facts', 'POST')
def add_fact(request):
    print(request['Resource'])
    fact = Fact(**request['params'])
    print(fact.id, fact.fact)
    return f'HTTP/1.1 303 See Other\r\nLocation: http://localhost:8888/facts/{fact.id}'


@Router.route(r'\/facts\/(\d+)')
def fact(request):
    fact_id = re.match(r'\/facts\/(\d+)', request['Resource']).group(1)
    csv_file = csv.reader(open('./facts.csv', "r"))
    for row in csv_file:
        if row[0] == fact_id:
            fact = Fact(row[0], row[1])
    response = Response('fact', {'fact': fact})
    return response


@Router.route(r'\/facts\/new')
def new_fact(request):
    return Response('form')
