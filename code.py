# Base Imports
import board
import supervisor
import digitalio
import storage
import usb_cdc
import usb_hid

# KMK Base Imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

# KMK Extension Imports
from kmk.extensions.international import International
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

# KMK Module Imports
from kmk.modules.combos import Combos
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot
from kmk.modules.tapdance import TapDance
from kmk.modules.dynamic_sequences import DynamicSequences

# KMK Kyeboard Setup
keyboard = KMKKeyboard()
keyboard.col_pins = (board.D4, board.D6) # Cols
keyboard.row_pins = (board.D0, board.D2) # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# KMK Extensions Enable
keyboard.extensions.append(International())
locks = LockStatus()
keyboard.extensions.append(locks)
keyboard.extensions.append(MediaKeys())
rgb = RGB(pixel_pin=board.NEOPIXEL, num_pixels=1, hue_default = 0, sat_default=0, val_default=100)
keyboard.extensions.append(rgb)

# KMK Modules Enable
combos = Combos()
keyboard.modules.append(combos)
keyboard.modules.append(Layers())
holdtap = HoldTap()
keyboard.modules.append(holdtap)
keyboard.modules.append(MouseKeys())
oneshot = OneShot()
keyboard.modules.append(oneshot)
tapdance = TapDance()
keyboard.modules.append(tapdance)
keyboard.modules.append(DynamicSequences())

# Keys
# http://kmkfw.io/docs/
KEY_1 = KC.HT(KC.MEDIA_PLAY_PAUSE, KC.RGB_TOG, tap_time=300)  # Play-Pause / LED toggle
KEY_2 = KC.AUDIO_VOL_UP                                       # Volume Up
KEY_3 = KC.AUDIO_MUTE                                         # Toggle Mute
KEY_4 = KC.AUDIO_VOL_DOWN                                     # Volume Down

# Keymap
keyboard.keymap = [
    [KEY_1, KEY_2,
     KEY_3, KEY_4]
]

# Run the keyboard
if __name__ == '__main__':
    keyboard.go()
