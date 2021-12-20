import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, 480, brightness=0.2)

dots.fill((0,0,0))
