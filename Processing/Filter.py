class Filter:

    def __init__(self, filterName, orientation='none', filterIntensity=(5, 5), zoomValue=0, rgb1=(1,2,3), rgb2=(1,2,3)):
        self.FILTER_NAME = filterName
        self.FilterIntensity = filterIntensity
        self.orientation = orientation
        self.zoomValue = zoomValue
        self.RGB1 = rgb1
        self.RGB2 = rgb2


