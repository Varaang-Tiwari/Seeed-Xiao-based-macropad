import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

for x in range(0, 5):

	led.value = False
	time.sleep(0.2)
	led.value = True
	time.sleep(0.2)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.UP

d1 = DigitalInOut(board.D1)
d1.direction = Direction.INPUT
d1.pull = Pull.UP

d2 = DigitalInOut(board.D2)
d2.direction = Direction.INPUT
d2.pull = Pull.UP

d3 = DigitalInOut(board.D3)
d3.direction = Direction.INPUT
d3.pull = Pull.UP

d4 = DigitalInOut(board.D4)
d4.direction = Direction.INPUT
d4.pull = Pull.UP

d5 = DigitalInOut(board.D5)
d5.direction = Direction.INPUT
d5.pull = Pull.UP

d6 = DigitalInOut(board.D6)
d6.direction = Direction.INPUT
d6.pull = Pull.UP

d7 = DigitalInOut(board.D7)
d7.direction = Direction.INPUT
d7.pull = Pull.UP

def open_app(app):
	kbd.send(Keycode.COMMAND, Keycode.SPACE)
	time.sleep(0.2)
	layout.write(app)
	time.sleep(0.2)
	kbd.send(Keycode.ENTER)

while True:

    if not d0.value:

    	led.value = False # led on
    	open_app("Chrome.app")
        time.sleep(0.5) 
        kbd.send(Keycode.COMMAND, Keycode.T)
        time.sleep(0.2)
        layout.write('https://mail.google.com')
        time.sleep(0.5)
        kbd.send(Keycode.ENTER)
        time.sleep(0.5)
        led.value = True # led off

    if not d1.value:

    	led.value = False # led on
    	open_app("~")
        led.value = True # led off
        time.sleep(0.5)  # debounce delay

    if not d2.value:

    	led.value = False # led on
    	open_app("terminal.app")
        time.sleep(0.5)  # debounce delay
        led.value = True # led off        

    if not d3.value:

    	led.value = False # led on
    	open_app("notes.app")
        time.sleep(0.5)  # debounce delay
        led.value = True # led off

    if not d4.value:

    	led.value = False # led on
    	open_app("Amazon Music.app")
        time.sleep(0.5)  # debounce delay
        led.value = True # led off        

    if not d5.value:

    	led.value = False # led on
    	kbd.send(Keycode.V)
        time.sleep(0.3)  # debounce delay
        led.value = True # led off

    if not d6.value:

    	led.value = False # led on
    	open_app("messages.app")
        time.sleep(0.3)  # debounce delay
        led.value = True # led off
        
    if not d7.value:

    	led.value = False # led on
    	kbd.send(Keycode.M)
        time.sleep(0.3)  # debounce delay
        led.value = True # led off