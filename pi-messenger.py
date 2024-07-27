from gpiozero import Button
from time import sleep

# I'm using a 4-button keyboard with a shared power line, resulting in 5 total connections.
# Since I just plugged it straight into the 40-pin header I will use GPIO pins 6, 13, and 19 and 26; they're conviniently placed in a row next to a ground pin.
# My keyboard is wired as follows:
# 1: Shared line (ground/physical pin 39)
# 2: Button 3 (GPIO 26/physical pin 37)
# 3: Button 4 (GPIO 19/physical pin 35)
# 4: Button 1 (GPIO 13/physical pin 33)
# 5: Button 2 (GPIO 6/physical pin 31)
# If you wish to use different controls, change the following part part

# Configure GPIO pins
# Ground is connected to physical pin 39
button1 = Button(13)
button2 = Button(6)
button3 = Button(26)
button4 = Button(19)

button1.when_pressed = lambda: print("Button 1 pressed")
button2.when_pressed = lambda: print("Button 2 pressed")
button3.when_pressed = lambda: print("Button 3 pressed")
button4.when_pressed = lambda: print("Button 4 pressed")

# Wait for input
sleep(60)