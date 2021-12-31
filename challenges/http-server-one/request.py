from datetime import datetime


class Request:

    def __init__(self, data):
        self.attributes = dict()
        self.attach_date()
        self.parse_data(data)

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
        self.parse_headers(lines[1:])

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
