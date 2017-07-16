"""
Simple script for rendering a palette
"""
from PIL import Image
from image_writer import ImageWriter

import color

if __name__ == '__main__':
    img = Image.new('RGB', (16, 4), 'black')
    writer = ImageWriter(img)
    for x in color.nes_fceux:
        writer.write(x)

    scale = 32
    img = img.resize((img.size[0] * scale, img.size[1] * scale), Image.NEAREST)
    img.show()
