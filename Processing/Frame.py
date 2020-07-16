from PIL import Image
import requests
from io import BytesIO

from Processing import Filter

class Frame:
    Url = ""
    ImageName = ""
    #ExportFormat = ""
    _appliedFilters = []

    Path = ''
    #NewUrl = ''

    # def __init__(self, url, imageName, exportFormat):
    #     self.Url = url
    #     self.ImageName = imageName
    #     self.ExportFormat = exportFormat

    def __init__(self, url, imageName):
        self.Url = url
        self.ImageName = imageName


    def downloadAndSaveImage(self):
        #def getImageFromUrl(url, name, format):
        response = requests.get(self.Url)
        img = Image.open(BytesIO(response.content))
        path = '..\\OriginalPictures\\' + self.ImageName
        img = img.save(path)
        self.Path = path

    def appendAppliedFilters(self, filter):
        self._appliedFilters.append(filter)

#    def __delete__(self, instance):



