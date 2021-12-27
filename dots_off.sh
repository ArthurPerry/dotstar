#! /bin/bash

cd ~/dotstar/
kill -9 `cat xmas_show.pid`
killall -9 python3
python3 dotstar_off.py
rm xmas_show.pid
