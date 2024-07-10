from abc import ABC , abstractmethod
from Entity.Entity_donwload import entity_donwload



class implement_video (ABC):

    @abstractmethod
    def donwload_video(self, Url:entity_donwload):
        pass

    @abstractmethod
    def donwload_music(self, Url:entity_donwload):
        pass