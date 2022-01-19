from datetime import datetime


class Event:

    def __init__(self, event):
        self.read_event(event)
        # self.name
        # self.id
        # self.url
        # self.info
        # self.please_note
        # self.price_range
        # self.start_date
        # self.end_date
        # self.dates
        # self.venue_name
        # self.venue_id
        # self.city
        # self.state
        # self.state
        # self.address
        # self.postal_code
        # self.longitude
        # self.latitude

    def __str__(self):
        return f"\n{self.name}\n{self.venue_name}\n{self.price_range}\n{self.dates}"

    def read_event(self, event):
        self.name = event['name']
        self.id = event['id']
        self.url = event['url']
        try:
            self.info = event['info']
        except KeyError:
            self.info = None
        try:
            self.please_note = event['pleaseNote']
        except KeyError:
            self.please_note = None
        try:
            self.price_range = self.get_price_range(event['priceRanges'])
        except KeyError:
            self.price_range = 'No Price Range'
        try:
            self.img = event['images'][0]['url']
        except KeyError:
            self.img = None
        self.read_dates = self.read_dates(event['dates'])
        try:
            self.read_venue(event['_embedded']['venues'][0])
        except KeyError:
            self.venue_name = None
            self.venue_id = None
            self.city = None
            self.state = None
            self.country = None
            self.address = None
            self.postal_code = None
            self.longitude = None
            self.latitude = None

    def get_price_range(self, priceRanges):
        min = priceRanges[0]['min']
        max = priceRanges[0]['max']
        if min != max:
            return f'${min:,.2f} - ${max:,.2f}'
        else:
            return f'${min:,.2f}'

    def read_dates(self, dates):
        try:
            date_string = dates['start']['localDate']
            date = datetime.fromisoformat(date_string)
            datetime_object = datetime.strptime(str(date.month), "%m")
            month = datetime_object.strftime("%b")
            self.start_date = f'{month} {date.day}'
        except KeyError:
            self.start_date = None
        try:
            date_string = dates['end']['localDate']
            date = datetime.fromisoformat(date_string)
            datetime_object = datetime.strptime(str(date.month), "%m")
            month = datetime_object.strftime("%b")
            self.end_date = f'{month} {date.day}'
        except KeyError:
            self.end_date = None
        if self.end_date is None:
            self.dates = f'{self.start_date}'
        elif self.end_date is not None:
            self.dates = f'{self.start_date} - {self.end_date}'
        elif self.end_date is None and self.start_date is None:
            self.dates = f'TBD'

    def read_venue(self, venue):
        try:
            self.venue_name = venue['name']
        except KeyError:
            self.venue_name = None
        try:
            self.venue_id = venue['id']
        except KeyError:
            self.venue_id = None
        try:
            self.city = venue['city']['name']
        except KeyError:
            self.city = None
        try:
            self.state = venue['state']['name']
        except KeyError:
            self.state = None
        try:
            self.country = venue['country']
        except KeyError:
            self.country = None
        try:
            self.address = venue['address']
        except KeyError:
            self.address = None
        try:
            self.postal_code = venue['postalCode']
        except KeyError:
            self.postal_code = None
        try:
            self.longitude = venue['location']['longitude']
        except KeyError:
            self.longitude = None
        try:
            self.latitude = venue['location']['latitude']
        except KeyError:
            self.latitude = None
