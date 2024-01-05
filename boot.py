import board
import digitalio
import storage
import usb_cdc
import usb_hid
import neopixel
import time

# Col and Row for key 1
col = digitalio.DigitalInOut(board.D4)
row = digitalio.DigitalInOut(board.D0)

# COL2ROW Diode direction
col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

# Neopixel setup
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 1

# If key 1 is not pressed disable usb drive
if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)
else:
    # Show configuration mode pixel indicator
    led[0] = (255,0,0)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.5)
    led[0] = (255,0,0)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.5)
    led[0] = (255,0,0)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.5)

row.deinit()
col.deinit()
