import bitstring
from PIL import Image
import sys
import math
import os
import color
from concurrent.futures import ThreadPoolExecutor

from image_writer import ImageWriter


def merge_images(image1, image2):
    """
    Merge two images into one, displayed side by side
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

def draw_bitstring(bitcount, data, func, width = 64, scale = 8):
    """
    Draw a bit string to an image
    """
    bits = bitstring.Bits(data)
    size = int(len(bits) / bitcount)
    dimensions = (width, int(math.ceil(size / float(width))))
    stream = bitstring.ConstBitStream(bits)
    img = Image.new('RGB', dimensions, 'black')
    writer = ImageWriter(img)
    fmt = 'uint:{0}'.format(bitcount)
    for _ in range(size):
        byte = stream.read(fmt)
        writer.write(func(byte))
    print(img.size)
    return img.resize((img.size[0] * scale, img.size[1] * scale), Image.NEAREST)


def draw_byte_pattern(bitcount, offsets, data, func, width = 64, scale = 8):
    """
    Draw a bit string to an image. Takes multiple samples per byte
    """
    bits = bitstring.Bits(data)
    size = int(len(bits) / 8)
    dimensions = (width, int(math.ceil(size * len(offsets) / float(width))))
    stream = bitstring.ConstBitStream(bits)
    img = Image.new('RGB', dimensions, 'black')
    writer = ImageWriter(img)
    fmt = 'uint:{0}'.format(bitcount)
    for _ in range(size):
        for i in offsets:
            stream.pos += i
            byte = stream.peek(fmt)
            stream.pos -= i
            writer.write(func(byte))
        stream.pos += 8
    return img.resize((img.size[0] * scale, img.size[1] * scale), Image.NEAREST)



