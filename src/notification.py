import sys
import cowsay

def bell_notification():
    sys.stdout.write('\a')
    sys.stdout.flush()

def beep_notification():
    from beepy import beep
    beep(sound=1)

def meow(message):
	cowsay.meow(message)