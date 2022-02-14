# dotstar
A set of python scripts to animate Dotstar strip that has been affixed to a Christmas Tree wireform.

run_show.sh will run the set of scripts

dots_off.sh will stop the run_show.sh script and turn of the strip.

## Prerequisites:
- Install [CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
- Install [Dotstar Library](https://learn.adafruit.com/adafruit-dotstar-leds/python-circuitpython)


## Homebridge Automation
Use [cmdSwitch2](https://github.com/luisiam/homebridge-cmdswitch2#readme) plugin with the following configuration to turn on / off animation script.

```
{
    "platform": "cmdSwitch2",
    "name": "cmdSwitch2",
    "synchronous": true,
    "switches": [
        {
            "name": "RPi Tree",
            "on_cmd": "ssh pi@192.168.1.197 /home/pi/dotstar/run_show.sh",
            "off_cmd": "ssh pi@192.168.1.197 /home/pi/dotstar/dots_off.sh",
            "state_cmd": "ssh pi@192.168.1.197 test -f /home/pi/dotstar/xmas_show.pid",
            "polling": true,
            "interval": 6,
            "timeout": 3
        }
    ]
}
```
