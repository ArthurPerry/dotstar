import board
import adafruit_dotstar
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.color import RED, PURPLE, AMBER, JADE, MAGENTA, ORANGE, TEAL
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

clock_pin = board.SCK
data_pin = board.MOSI
pixel_num = 460

pixels = adafruit_dotstar.DotStar(clock_pin, data_pin, pixel_num,
                                  brightness=0.2, auto_write=False)

blink = Blink(pixels, speed=0.5, color=JADE)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=AMBER)
colorcycle = ColorCycle(pixels, 0.5, colors=[MAGENTA, ORANGE, TEAL])
pulse = Pulse(pixels, speed=0.1, color=AMBER, period=3)
rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.01, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.01, num_sparkles=15)
sparkle = Sparkle(pixels, speed=0.05, color=AMBER, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=JADE)

animations = AnimationSequence(
                 blink, comet, chase, colorcycle, pulse, rainbow, rainbow_chase, rainbow_comet, rainbow_sparkle, sparkle, sparkle_pulse,
                 advance_interval=3, auto_clear=True)


while True:
    animations.animate()


