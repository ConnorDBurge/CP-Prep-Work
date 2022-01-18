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
        self.read_dates = self.read_dates(event['dates'])
        self.read_venue(event['_embedded']['venues'][0])

    def get_price_range(self, priceRanges):
        min = priceRanges[0]['min']
        max = priceRanges[0]['max']
        if min != max:
            return f'${min:,.2f} - ${max:,.2f}'
        else:
            return f'${min:,.2f}'

    def read_dates(self, dates):
        try:
            self.start_date = dates['start']['localDate']
        except KeyError:
            self.start_date = None
        try:
            self.end_date = dates['end']['localDate']
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
            self.city = venue['city']
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
