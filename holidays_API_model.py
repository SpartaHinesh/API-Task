class Holidays_model:
    def __init__(self, type_of_holiday):
        self.title = type_of_holiday['england-and-wales']['events']['title']
        self.date = type_of_holiday['england-and-wales']['events']['date']