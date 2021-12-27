trap "exit" INT TERM ERR
trap "kill 0" EXIT

while :
do
    python3 dotstar_circuitpytest.py
    python3 dotstar_chase.py
    python3 dotstar_random.py
    python3 dotstar_tree.py
done

