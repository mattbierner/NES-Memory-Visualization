"""
Visualize multiple memory dumps and combine them with game screenshots
"""
import sys
import math
import os
import color
import argparse
from PIL import Image

from concurrent.futures import ThreadPoolExecutor
from generate_image import draw_bitstring, merge_images

def generate_image(input_image, input_data, output_file):
    screenshot_scale = 1
    screenshot = Image.open(input_image)
    screenshot = screenshot.resize((screenshot.size[0] * screenshot_scale, screenshot.size[1] * screenshot_scale), Image.NEAREST)

    with open(input_data, 'rb') as f:
        data = bytearray(f.read())

    img = draw_bitstring(2, data, color.lookup(color.gameboy), width = 128, scale = 4)

    out = merge_images(screenshot, img)
    out.save(output_file)
    print(output_file)
    return output_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize multiple memory dumps and combine them with game screenshots')
    parser.add_argument('input', help='Input directory of images')
    parser.add_argument('output', help='Output directory for generated images')

    parser.add_argument('--start', type=int, help='Starting frame', default=0)
    parser.add_argument('--end', type=int, help='Ending frame', default=sys.maxsize)

    args = parser.parse_args()

    input = args.input
    output = args.output
    if not os.path.exists(output):
        os.makedirs(output)

    with ThreadPoolExecutor(max_workers=4) as executor:
        index = 0
        for i in range(args.start, args.end):
            input_image = os.path.join(input, '{0}.png'.format(i))
            if not os.path.exists(input_image):
                break
            input_data = os.path.join(input, '{0}.data'.format(i))
            output_file = os.path.join(output, '{0}.png'.format(index))
            index = index + 1
            r = executor.submit(generate_image, input_image, input_data, output_file)
        executor.shutdown(True)