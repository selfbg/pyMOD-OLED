from oled import OLED
from oled import Graphics
from PIL import Image

import sys


# Connect to the display on /dev/i2c-1
dis = OLED(1)

# Start communication
dis.begin()

# Start basic initialization
dis.initialize()

# Do additional configuration
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)

# Clear display
dis.clear()


files = ["CLOWN1.BMP", "CLOWN2.BMP", "CLOWN3.BMP", "CLOWN4.BMP", "CLOWN5.BMP", "CLOWN6.BMP", "CLOWN7.BMP", "CLOWN8.BMP"]
while True:

    for file in files:
        img = Image.open("clowns/" + file)

        w = img.size[0]
        h = img.size[1]

        for i in range(0, w):
            for j in range(0, h):
                xy = (i, j)
                if img.getpixel(xy):
                    Graphics.draw_pixel(i, j, False)
                else:
                    Graphics.draw_pixel(i, j, True)


        dis.update()

