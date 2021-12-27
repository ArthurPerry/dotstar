#! /bin/bash

if test -f "projects/dotstar-proj/adafruit_dotstar/examples/xmas_show.pid"; then
    ./dots_off.sh
fi

cd projects/dotstar-proj/adafruit_dotstar/examples/
./xmas_show.sh &
echo $! > xmas_show.pid

