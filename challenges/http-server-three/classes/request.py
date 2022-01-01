from datetime import datetime
from classes.facts import Fact
import re


class Request:

    def __init__(self, data):
        self.attributes = dict()
        self.attach_date()
        self.parse_data(data)
        # print(str(self))

    def __str__(self):
        string = '\n'
        for key, value in self.attributes.items():
            string += f'{key}: {value}\n'
        return string

    def attach_date(self):
        now = datetime.now()
        date_time = now.strftime('%m/%d/%Y %H:%M:%S')
        self.attributes['Date'] = date_time

    def parse_data(self, data):
        lines = data.split('\r\n')
        self.parse_status_line(lines[0])
        self.parse_headers(lines[1:-1])
        if self.attributes['Method'] == 'POST':
            self.parse_body(lines[-1])

    def parse_status_line(self, line):
        status_line_split_on_space = line.split(' ')
        self.attributes['Method'] = status_line_split_on_space[0]
        self.attributes['Resource'] = status_line_split_on_space[1]
        self.attributes['Protocol'] = status_line_split_on_space[2]

    def parse_headers(self, headers):
        for line in headers:
            if line != '':
                line_split = line.split(': ', 1)
                name = line_split[0]
                value = line_split[1]
                self.attributes[name] = value

    def parse_body(self, body):
        param_dict = dict()
        body_split_on_ampers = body.split('&')
        for param in body_split_on_ampers:
            values = param.split('=', 1)
            param_dict['fact'] = values[1].replace('+', ' ')
            param_dict['id'] = Fact.fact_id + 1
            param_dict['new_fact'] = True
        self.attributes['params'] = param_dict
