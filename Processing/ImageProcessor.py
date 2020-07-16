from Processing.Frame import Frame
from Processing.Filter import Filter
from PIL import Image, ImageOps
import numpy as np
import cv2
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from matplotlib import pyplot as plt
#todo remove matplotlib from venv

from API.test2 import ASCIIFIER

class ImageProcessor(object):

    @staticmethod
    def applyFiltersToImage(frame, filters):
        frame.downloadAndSaveImage()
        for filter in filters:
            frame = ImageProcessor.applyFilter(frame, filter)

        return frame

    @staticmethod
    def applyFilter(frame, filter):
        #frame.downloadAndSaveImage()
        # if filter.FILTER_CATEGORY == 'BLUR':
        if filter.FILTER_NAME == 'GAUSSIAN_BLUR':
            #todo refacto into same function
            e = frame.Path
            img = cv2.imread(e)
            blur = cv2.blur(img, (50, 50))
            # newFrameName = frame.ImageName + frame.ExportFormat
            path = '..\\ProcessedPictures\\' + frame.ImageName
            cv2.imwrite(path, blur)
            #frame = Frame('', newFrameName)
            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'GRAYSCALE':
            #todo add intensity for filter
            e = frame.Path
            img = cv2.imread(e)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            cv2.imwrite(path, gray)
            #frame = Frame('', newFrameName)
            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'COLOR_INVERSION':
            e = frame.Path
            im = Image.open(e)
            im_invert = ImageOps.invert(im)
            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            im_invert.save(path, quality=95)
            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'ZOOM':
            #todo check params
            e = frame.Path
            image = cv2.imread(e)
            height, width, channels = image.shape
            oHeight, oWidth = height, width
            centerX, centerY = int(height * 1.5), int(width * 1.5)
            resized_cropped = cv2.resize(image, (centerY, centerX))
            height, width, channels = resized_cropped.shape
            x = int(width * 0.25)
            w = oWidth
            y = int(height * 0.25)
            h = oHeight
            cropped = resized_cropped[y:y + h, x:x + w]
            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            cv2.imwrite(path, cropped)
            # frame = Frame('', newFrameName)
            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'COMPRESSION':
            #todo check params
            e = frame.Path
            img = Image.open(e)
            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            img.save(path, optimize=True, quality=55)
            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'RADIAL_BLUR':
            e = frame.Path
            img = cv2.imread(e)
            #todo set as param value of filter
            if filter.FilterIntensity == 0:
                filter.FilterIntensity = 1

            kernel_size = int(filter.FilterIntensity * 1.5)
            kernel_v = np.zeros((kernel_size, kernel_size))
            kernel_h = np.copy(kernel_v)

            kernel_v[:, int((kernel_size - 1) / 2)] = np.ones(kernel_size)
            kernel_h[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)

            kernel_v /= kernel_size
            kernel_h /= kernel_size

            #todo check if orientation vertical or horizontal
            vertical_mb = cv2.filter2D(img, -1, kernel_v)
            horizontal_mb = cv2.filter2D(img, -1, kernel_h)

            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            if filter.orientation == 'vertical':
                cv2.imwrite(path, vertical_mb)
            elif filter.orientation == 'horizontal':
                cv2.imwrite(path, horizontal_mb)

            # frame = Frame('', newFrameName)
            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'ASCII_IMAGE_CONVERSION':
            e = frame.Path
            #img = Image.open(e)
            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            original = '..\\OriginalPictures\\' + newFrameName

            ASCIIFIER.ASCII(frame.Url, path)

            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

        if filter.FILTER_NAME == 'BICHROMATIC':
            e = frame.Path
            image = cv2.imread(e)
            newFrameName = frame.ImageName
            path = '..\\ProcessedPictures\\' + newFrameName
            original = '..\\OriginalPictures\\' + newFrameName

            height, width, channels = image.shape
            blk = np.zeros(image.shape, np.uint8)
            colors = [(166, 64, 0), (255, 77, 202), (169, 230, 77), (197, 77, 234), (200, 77, 130), (95, 190, 77)]
            #import random
            #color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

            x0,y0,z0 = filter.RGB1
            x1,y1,z1 = filter.RGB2

            filter.RGB1 = (z0, y0, x0)
            filter.RGB2 = (z1, y1, x1)
            print(filter.RGB1)
            print(filter.RGB2)


            cv2.rectangle(blk, (0, 0), (int(width/2), height),
                          filter.RGB1, cv2.FILLED)

            cv2.rectangle(blk, (int(width/2), 0), (width, height),
                          filter.RGB2, cv2.FILLED)
            out = cv2.addWeighted(image, 1.0, blk, 0.5, 1)
            cv2.imwrite(path, out)

            frame.Path = path
            frame.NewUrl = frame.Path
            return frame

#ImageProcessor.applyFiltersToImage(Frame('https://ichef.bbci.co.uk/news/410/cpsprodpb/10145/production/_112216856_gettyimages-1184274010.jpg', 'obama.jpg'), [Filter('BICHROMATIC')])


