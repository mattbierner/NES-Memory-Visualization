import math

class ImageWriter(object):
    def __init__(self, img):
        self.pixels = img.load()
        self.index = 0
        self.width = img.size[0]
        self.height = img.size[1]

    def write(self, data):
        x = self.index % self.width
        y = math.floor(self.index / float(self.width))
        self.pixels[x, y] = data
        self.index = self.index + 1
