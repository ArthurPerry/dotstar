import time
import board
import adafruit_dotstar
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.color import RED, PURPLE, AMBER, JADE, MAGENTA, ORANGE, TEAL,WHITE,OLD_LACE
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.helper import PixelMap

clock_pin = board.SCK
data_pin = board.MOSI
pixel_num = 446

pixels = adafruit_dotstar.DotStar(clock_pin, data_pin, pixel_num,
                                  brightness=0.2, auto_write=False)

# Define tree parts
tree_trunk = PixelSubset(pixels, 0 ,  29)
tree_bottom2 = PixelSubset(pixels, 221 ,  259)
tree_bottom1 = PixelSubset(pixels, 30 ,  62)
tree_left = PixelSubset(pixels, 63 , 141) 
tree_right = PixelSubset(pixels, 142 ,  220)
tree_cross1 = PixelSubset(pixels, 262 ,  308)
tree_cross2 = PixelSubset(pixels, 320 ,  357)
tree_cross3 = PixelSubset(pixels, 371 ,  400)
tree_cross4 = PixelSubset(pixels, 411 ,  429)
tree_cross5 = PixelSubset(pixels, 437 ,  446)


tree_outline = PixelSubset(pixels, 0 ,  259)
tree_inside = PixelMap(pixels, [(262,308),(320,357),(371,400),(411,429),(437,446)], individual_pixels=False)


#blink = Blink(outline, speed=0.5, color=JADE)
#comet = Comet(inside, speed=0.05, color=PURPLE, tail_length=5, bounce=True)
#chase = Chase(inside, speed=0.1, size=3, spacing=6, color=AMBER)
#colorcycle = ColorCycle(pixels, 0.5, colors=[MAGENTA, ORANGE, TEAL])
#pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)
#rainbow = Rainbow(pixels, speed=0.1, period=2)
#rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
#rainbow_comet = RainbowComet(pixels, speed=0.01, tail_length=7, bounce=True)
#rainbow_sparkle = RainbowSparkle(pixels, speed=0.01, num_sparkles=15)
#sparkle = Sparkle(pixels, speed=0.05, color=AMBER, num_sparkles=10)
#sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=JADE)


animation_tree_outline = Chase(tree_outline, speed=0.5, color=JADE, size=8, spacing=5)
animation_tree_cross1 = Comet(tree_cross1, speed=0.05, color=PURPLE, tail_length=5, bounce=True )
animation_tree_cross2 = Comet(tree_cross2, speed=0.05, color=PURPLE, tail_length=5, bounce=True )
animation_tree_cross3 = Comet(tree_cross3, speed=0.05, color=PURPLE, tail_length=5, bounce=True )
animation_tree_cross4 = Comet(tree_cross4, speed=0.05, color=PURPLE, tail_length=5, bounce=True )
animation_tree_cross5 = Comet(tree_cross5, speed=0.05, color=PURPLE, tail_length=5, bounce=True )


animations = AnimationSequence(
     Blink(pixels, speed=0.5, color=JADE),
     AnimationGroup(
          Pulse(tree_outline, speed=0.1, color=JADE, period=3),
          RainbowSparkle(tree_cross1, speed=0.01, num_sparkles=15),
          RainbowSparkle(tree_cross2, speed=0.01, num_sparkles=15),
          RainbowSparkle(tree_cross3, speed=0.01, num_sparkles=15),
          RainbowSparkle(tree_cross4, speed=0.01, num_sparkles=15),
          RainbowSparkle(tree_cross5, speed=0.01, num_sparkles=15),
     ),
          AnimationGroup(
          animation_tree_outline, 
          animation_tree_cross1 ,
          animation_tree_cross2 ,
          animation_tree_cross3 ,
          animation_tree_cross4 ,
          animation_tree_cross5 

     ),
     Comet(pixels, speed=0.01, color=AMBER, tail_length=10, bounce=True ),
     SparklePulse(pixels, speed=0.5, color=JADE),
     AnimationGroup(
          Rainbow(tree_outline, speed=0.1, period=3),
          SparklePulse(tree_cross1, speed=0.05, period=3, color=WHITE),
          SparklePulse(tree_cross2, speed=0.05, period=3, color=WHITE),
          SparklePulse(tree_cross3, speed=0.05, period=3, color=WHITE),
          SparklePulse(tree_cross4, speed=0.05, period=3, color=WHITE),
          SparklePulse(tree_cross5, speed=0.05, period=3, color=WHITE)
     ),
     advance_interval=6, 
     auto_clear=True
)

timeout = time.time() + 48

while True:
     animations.animate()
     if time.time() > timeout:
          break


