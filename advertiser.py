from base_model import BaseAdvertiser

class Advertiser(BaseAdvertiser):
    advertisers = []
    def __init__(self,name):
        super().__init__()
        self._name = name
        Advertiser.advertisers.append(self)

    def get_name(self):
        print("Name", self._name)
        return self._name

    def set_name(self, name):
        self._name = name

    @staticmethod
    def help():
        print(f"This is help for advertiser class")

    @staticmethod
    def get_total_clicks():
        total_clicks = 0
        for advertiser in Advertiser.advertisers:
            total_clicks+=advertiser.get_click()
        print("total clicks are:",total_clicks)
        return total_clicks

    def describe_me(self):
        print("I am an advertiser class")