from gpiozero import Button

# I'm using a 4-button keyboard with a shared power line, resulting in 5 total connections.
# Since I just plugged it straight into the GPIO pins I will use GPIO pins 6, 13, and 19 and 26; they're conviniently placed in a row next to a ground pin.
# If you wish to use different controls, change this part

# Configure GPIO pins
button1 = Button(6)
button2 = Button(13)
button3 = Button(19)
button4 = Button(26)

button1.when_pressed = lambda: print("Button 1 pressed")
button2.when_pressed = lambda: print("Button 2 pressed")
button3.when_pressed = lambda: print("Button 3 pressed")
button4.when_pressed = lambda: print("Button 4 pressed")