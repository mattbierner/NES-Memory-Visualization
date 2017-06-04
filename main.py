import math
from PIL import Image

import color


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


def merge_images(image1, image2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result


def draw_bits(data):
    img = Image.new('RGB', (100, 200), "black")
    writer = ImageWriter(img)

    for b in data:
        for g in xrange(8):
            bit = (b >> g) & 1
            color = 255 if bit else 0
            writer.write((color, color, color))
    return img


def draw_bytes(data, func):
    width = 32
    height = int(math.ceil(len(data) / width))
    img = Image.new('RGB', (width, height), 'black')
    writer = ImageWriter(img)
    for byte in data:
        writer.write(func(byte))

    scale = 4
    return img.resize((img.size[0] * scale, img.size[1] * scale), Image.NEAREST)


if __name__ == '__main__':
    for i in xrange(300, 900):
        screen = Image.open('snaps/{0}.png'.format(i))
        with open('data/{0}.data'.format(i), 'rb') as f:
            data = bytearray(f.read())

        img = draw_bytes(data, color.luminance)

        out = merge_images(screen, img)
        out.save('out/{0}.png'.format(i))
