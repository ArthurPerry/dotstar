# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import random
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, 480, brightness=0.2)

# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32


# MAIN LOOP
n_dots = len(dots)
counter = 0

dots.auto_write = False
while True:
    dots.fill((0,0,0))
    # Fill each dot with a random color
    for dot in range(n_dots):
        if (dot % 2) == (counter % 2):
       	    #dots[dot] = (random_color(), random_color(), random_color())
            dots[dot] = (255,0,0)
        else:
            dots[dot]=(0,255,0)

    dots.show()
    counter += 1
    time.sleep(0.5)
