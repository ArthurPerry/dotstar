import random 
import time
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
pixels = dotstar.DotStar(board.SCK, board.MOSI, 480, brightness=0.2, auto_write=False)

tree = {
    "trunk"   : {"start":   0 , "end":  29},
    "bottom1" : {"start":  30 , "end":  62},
    "bottom2" : {"start": 221 , "end": 259},
    "left"    : {"start":  63 , "end": 141},
    "right"   : {"start": 142 , "end": 220},
    "cross1"  : {"start": 262 , "end": 308},
    "cross2"  : {"start": 320 , "end": 357},
    "cross3"  : {"start": 371 , "end": 400},
    "cross4"  : {"start": 411 , "end": 429},
    "cross5"  : {"start": 437 , "end": 446},
}

outline = ("bottom1","bottom2","left","right")
inside = ("cross1","cross2","cross3","cross4","cross5")
triangle = outline + inside 
all = outline + inside + (("trunk",))

COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)
COLOR_BROWN = (165,42,42)
COLOR_OFF = (0,0,0)
 
def paint(partname, color):
    part = tree[partname]
    partlen = part["end"] - part["start"]
    pixels[part["start"]:part["end"]] = [color] * partlen
    pixels.show()

def paint_split(partname, color1,color2):
    part = tree[partname]
    partlen = part["end"] - part["start"]
    pixels[part["start"]:part["end"]] = [color1] * partlen
    for i in range(partlen):
        if i%3 == 0:
            pixels[part["start"]+i] = color2
    pixels.show()

def paint_sparkle(partname, color):
    part = tree[partname]
    partlen = part["end"] - part["start"]
    pixels[part["start"]:part["end"]] = [color] * partlen
    for i in range(partlen // 9):
        dot = random.randrange(part["start"],part["end"] )
        pixels[dot] = (random_color(), random_color(), random_color())
    pixels.show()
    time.sleep(0.05)

def paint_chase(partname, color, wait):
    part = tree[partname]
    partlen = part["end"] - part["start"]
    for i in range(partlen):
        pixels[part["start"] + i] = color
        pixels.show()
        time.sleep(wait) 
    

# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32

paint("trunk",COLOR_BROWN)
for part in outline :
    paint(part,COLOR_GREEN)

for i in range(20):
    for part in inside :
        if i%2 == 0:
            paint_split(part,COLOR_GREEN,COLOR_RED)
        else:
            paint_split(part,COLOR_GREEN,COLOR_OFF)
    time.sleep(.1)


for part in all :
    paint (part, COLOR_BLUE)
time.sleep(2)

for part in inside:
    paint_chase(part, (random_color(), random_color(), random_color()), 0.05)

for part in outline:
    paint_chase(part, (random_color(), random_color(), random_color()), 0.05)

for part in outline :
    paint(part,COLOR_GREEN)

timeout = time.time() + 15
while True:
    for part in inside:
        paint_sparkle(part,COLOR_GREEN) 
    if time.time() > timeout:
        break

pixels.fill(COLOR_OFF) 
pixels.show()
