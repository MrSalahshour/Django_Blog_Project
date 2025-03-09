from abc import ABC, abstractmethod
class BaseAdvertiser(ABC):
    id_counter = 0
    def __init__(self):
        self._id = BaseAdvertiser.id_counter
        BaseAdvertiser.id_counter+=1
        self._clicks = 0
        self._views = 0

    def get_click(self):
        print("number of click for this class are:",self._clicks)
        return self._clicks

    def get_views(self):
        return self._views

    def inc_clicks(self):
        self._clicks+=1

    def inc_views(self):
        self._views+=1

    @abstractmethod
    def describe_me(self):
        pass




