from PIL import Image
import requests
from io import BytesIO

def getImageFromUrl(url, name, format):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    path = '..\\OriginalPictures\\' + name + '.' + format
    img = img.save(path)
    return path