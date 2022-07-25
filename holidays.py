from holidays_API_model import Holidays_model
import requests

class single_holiday:

    def __int__(self, b_holiday):
        self.url = "https://www.gov.uk/bank-holidays.json/"+b_holiday
        self.request = requests.get(self.url)
        self.resp_json = self.request.json()

    def response_data(self):
        return Holidays_model(self.resp_json)