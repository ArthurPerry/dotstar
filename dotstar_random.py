# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import random
import board
import adafruit_dotstar as dotstar

## Tree Mapping
## trunk 0-29
## bottom 30-62, 221-249
## left 63-141
## right 142-220
## cross1  262-308
## cross2  320-357
## cross3  371-400
## cross4  411-429
## cross5  443-452


# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, 480, brightness=0.2)

# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32


# MAIN LOOP
n_dots = len(dots)

dots.auto_write = False

timeout = time.time() + 30

while True:
    dots.fill((0,0,0))
    for i in range(10):
        dot = random.randrange(0, n_dots)
        dots[dot] = (random_color(), random_color(), random_color())
    dots.show()
    time.sleep(0.05)
#    dots[dot] = ((0,0,0))
#    dots.show()
    if time.time() > timeout:
        break
