""" Model a record """


class Record(object):
    def __init__(self, gps_lat=None, gps_long=None, company_name=None, search_url=None,
                 xpath_pattern=None, company_email=None):

        self.gps_lat = gps_lat
        self.gps_long = gps_long
        self.company_name = company_name
        self.search_url = search_url
        self.xpath_pattern = xpath_pattern
        self.company_email = company_email

        self.validate()

    def validate(self):
        # basic check
        if not self.gps_lat.isdecimal():
            self.gps_lat = 0.0
        else:
            self.gps_lat = float(self.gps_lat)

        if not self.gps_long.isdecimal():
            self.gps_long = 0.0
        else:
            self.gps_long = float(self.gps_long)

        # append /text() to xpath so we get text values
        if not self.xpath_pattern.endswith("text()"):
            self.xpath_pattern += "/text()"
