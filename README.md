# dotstar
A set of python scripts to animate Dotstar strip that has been affixed to a Christmas Tree wireform.

run_show.sh will run the set of scripts

dots_off.sh will stop the run_show.sh script and turn of the strip.

## Prerequisites:
- Install [CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
- Install [Dotstar Library](https://learn.adafruit.com/adafruit-dotstar-leds/python-circuitpython)

## Service Installation
The service unit file [dotstar.service](dotstar.service) contains the configuration needed to start and stop the animation using `systemctl`.
```
# Copy the file to the service directory: 
sudo cp dotstar.service /lib/systemd/system/

# Set file permissions: 
sudo chmod 644 /lib/systemd/system/dotstar.service

# Reload the service daemon: 
sudo systemctl daemon-reload

# Test service start:
sudo systemctl start dotstar.service

# Test service stop:
sudo systemctl stop dotstar.service

# Get service status:
sudo systemctl status dotstar.service

# Test service is active:
sudo systemctl is-active dotstar.service

# Enable the service to start on boot 
sudo systemctl enable dotstar.service
```

## Homebridge Automation
Use [cmdSwitch2](https://github.com/luisiam/homebridge-cmdswitch2#readme) plugin with the following configuration to turn on / off animation script. Ensure that Homebridge is able to log into the remote system (i.e. use `ssh-copy-id` to copy the public key to the remote system)

```
{
    "platform": "cmdSwitch2",
    "name": "cmdSwitch2",
    "synchronous": true,
    "switches": [
        {
            "name": "RPi Tree",
            "on_cmd": "ssh pi@<ip-addr> sudo systemctl start dotstar.service",
            "off_cmd": "ssh pi@<ip-addr> sudo systemctl stop dotstar.service",
            "state_cmd": "ssh pi@<ip-addr> systemctl is-active  dotstar.service",
            "polling": true,
            "interval": 6,
            "timeout": 3
        }
    ]
}
```
