from base_model import BaseAdvertiser

class Ad(BaseAdvertiser):
    def __init__(self,title, img_url, link, advertiser):
        super().__init__()
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_img_url(self):
        return self._img_url

    def set_img_url(self, img_url):
        self._img_url = img_url

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    def get_advertiser(self):
        return self._advertiser

    def set_advertiser(self, advertiser):
        self._advertiser = advertiser

    def inc_clicks(self):
        super().inc_clicks()
        self.get_advertiser().inc_clicks()

    def describe_me(self):
        print("I am an ad class")
