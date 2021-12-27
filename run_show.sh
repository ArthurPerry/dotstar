#! /bin/bash

if test -f "~/dotstar/xmas_show.pid"; then
    ./dots_off.sh
fi

cd ~/dotstar/
./xmas_show.sh &
echo $! > xmas_show.pid

