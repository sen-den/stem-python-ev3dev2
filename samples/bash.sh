# Just beep
beep
# Beep with options - frequency, length, delay after and repenions number
beep -f 440 -l 100 -d 500 -r 2
# Beep with specified frequency and pause (Ctrl+C to stop)
while true; do beep -f 440 --debug && sleep 5; done
