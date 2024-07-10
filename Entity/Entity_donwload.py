class entity_donwload:
    def __init__(self , Url , ruta ):
        self.Url = Url
        self.ruta = ruta


    @property
    def getruta(self):
        return  self.__ruta

    @getruta.setter
    def setruta(self,ruta):
        self.ruta = ruta


    @property
    def geturl(self):
        return self.__Url

    @geturl.setter
    def seturl(self,Url):
        self.Url = Url

