import requests
import json
from Processing.ImageProcessor import ImageProcessor
from Processing.Frame import Frame
from Processing.Filter import Filter
from urllib.parse import urlparse
from PIL import ImageColor
import os

class Client:
    _user = []
    _authenticator = []
    #_endpointUnprocessed = 'http://23.102.34.223:8080/images/untreated'

    def __init__(self, user, authenticator):
        self._user = user
        self._authenticator = authenticator

    def _contructArrayOfFilters(self, filtersJson):
        # array = json.loads(filtersJson)
        filtersArr = []
        for element in filtersJson:
            if element['name'] == 'GAUSSIAN_BLUR':
                a = int(int(element['parameter'][0]['value']) / 3)
                filtersArr.append(Filter(element['name'], filterIntensity=(a, a)))
                continue
            if element['name'] == 'GRAYSCALE':
                a = int(element['parameter'][0]['value'])
                filtersArr.append(Filter(element['name'], filterIntensity=a))
                continue
            if element['name'] == 'COLOR_INVERSION':
                filtersArr.append(Filter(element['name'], element['parameter'][0]['value']))
                continue
            if element['name'] == 'ZOOM':
                filtersArr.append(Filter(element['name'], zoomValue=int(element['parameter'][0]['value'])))
                continue
            if element['name'] == 'COMPRESSION':
                #a = element['parameter'][0]
                filtersArr.append(Filter(element['name'], filterIntensity=int(element['parameter'][0]['value'])))
                continue

            if element['name'] == 'RADIAL_BLUR':
                filtersArr.append(Filter(element['name'],  orientation=element['parameter'][1]['value'], filterIntensity=int(int(element['parameter'][0]['value'])*1.25)))
                continue

            if element['name'] == 'ASCII_IMAGE_CONVERSION':
                filtersArr.append(Filter(element['name']))
                continue

            if element['name'] == 'BICHROMATIC':
                a = element['parameter'][0]['value']
                b = element['parameter'][1]['value']

                a = a[2:]
                a = '#'+a

                b = b[2:]
                b = '#' + b

                x = ImageColor.getcolor(a, "RGB")
                y = ImageColor.getcolor(b, "RGB")

                filtersArr.append(Filter(element['name'], rgb1=x, rgb2=y))
                continue

        return filtersArr

    def _getUnprocessedImages(self):
        #construct array of urls and ids and process them with corresponding filters
        #get all unprocessed images on url with get request

        url = 'http://23.102.34.223:8080/images/untreated'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self._authenticator.CURRENT_TOKEN}

        j = requests.get(url, headers=headers)

        parsed = json.loads(j.text)
        for element in parsed:
            del element['createdAt']
            del element['updatedAt']
            del element['treaty']
        for element in parsed:
            print(element)
        return parsed
            # print('\n')
        # print(parsed[0])
        #print(json.dumps(parsed, indent=2))

    def _processImages(self, unprocessedImages):
        # get array of unprocImages and uses ImageProcessor for processing all that (async->future)
        # construct array of id's and paths to images and return it

        #a = unprocessedImages[1]['filters']
        for element in unprocessedImages:
            filters = self._contructArrayOfFilters(element['filters'])
            del element['filters']

            #for filter in filters:
            b = element['urlUntreated']
            a = urlparse(element['urlUntreated'])
            e = str(os.path.basename(a.path))
            ee = os.path.splitext(e)[0]
            v = os.path.splitext(e)
            myFrame = Frame(b, ee + v[1])

            c = ImageProcessor.applyFiltersToImage(myFrame, filters)

            element['urlTreated'] = c.Path
            # if filter == filters[-1]:
            #     element['url'] = c.Path

            debug = 1

            print(element)
            print('\n')

        return unprocessedImages

    def _sendImages(self, endpointToSend, processedImages):
        # send processed stuff to treated endpoint
        # create a delay on a foreach loop for each image and send them one by one after delay or getting 200
        c = 4

        for element in processedImages:
            multipart_form_data = {'image': (os.path.basename(element['urlTreated']), open(element['urlTreated'], 'rb'))}
            image = {'idImage': str(element['id'])}
            header = {'Authorization': 'Bearer ' + self._authenticator.CURRENT_TOKEN}
            response = requests.post('http://23.102.34.223:8080/images/treated', headers=header, files=multipart_form_data, params=image)


        return c

    def Start(self):
        #print(self._authenticator.AuthenticateUser(self._user) + '\n')
        if self._authenticator.AuthenticateUser(self._user) != '':
            print('User: ' + self._user.USEREMAIL + '\nAuthenticated with JWT' + ' ' + self._authenticator.CURRENT_TOKEN[0])

        unprocessedImages = self._getUnprocessedImages()
        #print(json.dumps(unprocessedImages, indent=2))
        processedImages = self._processImages(unprocessedImages)
        #if len(processedImage)==0:

        for element in processedImages:
            if not str(element['urlTreated']).startswith('..'):
                processedImages.remove(element)

        responseIsSucc = self._sendImages('http://23.102.34.223:8080/images/treated', processedImages)


