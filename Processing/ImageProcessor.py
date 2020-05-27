from Processing.Frame import Frame
from Processing import Filter
import cv2
import os

from matplotlib import pyplot as plt
#todo remove matplotlib from venv


class ImageProcessor(object):
    # todo add possibility of multiple imageProcessors for pipeline
    # _name = ''
    #
    # def __init__(self, name):
    #     self._name = name

    # returns new Image object
    @staticmethod
    def applyFilter(frame, filter):
        frame.downloadAndSaveImage()
        # if filter.FILTER_CATEGORY == 'BLUR':
        if filter.FILTER_NAME == 'GAUSSIAN_BLUR':
            #todo refacto into same function
            e = frame.Path
            img = cv2.imread(e)
            blur = cv2.blur(img, (5, 5))
            newFrameName = frame.ImageName + '_gaussBlur' + '.' + frame.ExportFormat
            path = '..\\ProcessedPictures\\' + newFrameName
            cv2.imwrite(path, blur)
            a = Frame('', newFrameName, frame.ExportFormat)
            a.Path = os.getcwd() + '\\' + newFrameName
            a.NewUrl = a.Path
            return a
        if filter.FILTER_NAME == 'GRAYSCALE':
            e = frame.Path
            img = cv2.imread(e)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFrameName = frame.ImageName + '_grayScale' + '.' + frame.ExportFormat
            path = '..\\ProcessedPictures\\' + newFrameName
            cv2.imwrite(path, gray)
            a = Frame('', newFrameName, frame.ExportFormat)
            a.Path = os.getcwd() + '\\' + newFrameName
            a.NewUrl = a.Path
            return a