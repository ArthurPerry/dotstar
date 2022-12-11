#! /bin/bash

cd /home/pi/dotstar/

if test -f "~/dotstar/xmas_show.pid"; then
    ./dots_off.sh
fi

./xmas_show.sh &
echo $! > xmas_show.pid

