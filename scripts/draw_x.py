"""
Simple script for rendering a palette
"""
from PIL import Image
from bitstring import BitArray, ConstBitStream
from image_writer import ImageWriter
import math
import color


eight = [
    (0, 0, 0),
    (0, 170, 170),
    (170, 0, 170),
    (170, 170, 170),
    (0, 255, 255),
    (85, 255, 255),
    (255, 85, 255),
    (255, 255, 255)
]

if __name__ == '__main__':
    img = Image.new('RGB', (16, 16), 'yellow')
    writer = ImageWriter(img)
    stream = ConstBitStream(BitArray('0b001001001001000100100100100011110001111'))
    fmt = 'uint:{0}'.format(3)
   
    if False:
        while stream.pos < 24:
            byte = stream.read(fmt)
            writer.write(eight[byte])
    elif True:
        byte = stream.read('uint:{0}'.format(24))
        for i in range(8):
            d = (byte >> (i * 3)) & 0b111
            print(d)
            writer.write(eight[d])
    else:
        byte = stream.read('uint:{0}'.format(24))
        for i in range(8):
            d = byte % 8
            byte = byte >> 3
            print(d)
            writer.write(eight[d])


    scale = 32
    img = img.resize((img.size[0] * scale, img.size[1] * scale), Image.NEAREST)
    img.show()
