from gpiozero import Button
from signal import pause
from os import getenv
from time import time
from requests import post
from dotenv import load_dotenv
load_dotenv()

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

# Minimum time between activations of the same button, in seconds
buttonCooldown = 60

# Timestamps for latest activation of each button
buttonActivationTimestamps = {
    'button1': 0,
    'button2': 0,
    'button3': 0,
    'button4': 0,
}


def send_sms(recipient: str, message: str | None = None):
    """
    Send an SMS using the 46elks API.
    :param recipient: The phone number to send the SMS to. Must be in E.164 format.
    :param message: The message to send. If falsy, uses a default message.
    """
    response = post(
        'https://api.46elks.com/a1/sms',
        auth=(getenv('46ELKS_API_USERNAME'), getenv('46ELKS_API_PASSWORD')),
        data={
            'from': 'RasPiMSGR',
            'to': recipient,
            'message': str(message or 'This is a test message.'),
        }
    )
    print(response.json() or response.text or "No response?")


# Define button actions, this is where you can customize the behavior of the buttons.


def button1_action():
    if time() - buttonActivationTimestamps['button1'] > buttonCooldown:
        send_sms(getenv('RECIPIENT_1'), getenv('ENV_MESSAGE'))
        buttonActivationTimestamps['button1'] = time()


def button2_action():
    if time() - buttonActivationTimestamps['button2'] > buttonCooldown:
        send_sms(getenv('RECIPIENT_2'), getenv('ENV_MESSAGE'))
        buttonActivationTimestamps['button2'] = time()


def button3_action():
    if time() - buttonActivationTimestamps['button3'] > buttonCooldown:
        send_sms(getenv('RECIPIENT_3'), getenv('ENV_MESSAGE'))
        buttonActivationTimestamps['button3'] = time()


def button4_action():
    if time() - buttonActivationTimestamps['button4'] > buttonCooldown:
        send_sms(getenv('RECIPIENT_4'), getenv('ENV_MESSAGE'))
        buttonActivationTimestamps['button4'] = time()


# Define button actions. Get recipient and message from environment variables.
button1.when_pressed = button1_action
button2.when_pressed = button2_action
button3.when_pressed = button3_action
button4.when_pressed = button4_action

# Wait for button presses
pause()
