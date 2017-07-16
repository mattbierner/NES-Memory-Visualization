import sys
import math
import os
import color
from PIL import Image
from generate_image import draw_bitstring, draw_byte_pattern, merge_images



def generate_image(input_data):
    with open(input_data, 'rb') as f:
        data = bytearray(f.read())

    return draw_byte_pattern(6, [0, 2], data, color.lookup(color.nes), width = 64, scale = 8)
    return draw_bitstring(8, data, color.expand(8, 6, color.lookup(color.nes)), width = 64, scale = 8)
    return draw_bitstring(6, data, color.lookup(color.nes), width = 64, scale = 8)






if __name__ == '__main__':
    input = sys.argv[1]
    img = generate_image(input)
    if len(sys.argv) >= 3:
        screenshot_scale = 2
        screenshot = Image.open(sys.argv[2])

        screenshot = screenshot.resize((screenshot.size[0] * screenshot_scale, screenshot.size[1] * screenshot_scale), Image.NEAREST)
        img = merge_images(screenshot, img)
    img.show()