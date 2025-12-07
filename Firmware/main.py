import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

media = MediaKeys()
keyboard.extensions.append(media)

KEY_PINS = [ #SW 1-6
    board.A3,
    board.D0,
    board.D1,
    board.D2,
    board.D4,
    board.D3
]

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.F18,
    ]
]

encoder = EncoderHandler()

#GPIO mapping (for rot. encoder)
#A - GPIO26/A0
#B - GPIO28/A2
#SW - GPIO27/A1
encoder.pins = (
    (board.A0, board.A2, board.A1),
)

encoder.map = [
    (
        KC.VOLD,  #counter clockwise volume down
        KC.VOLU,  #clockwise volume up
        KC.MPLY,  #press fires play/pause
    ),
]

#todo: ADD OLED SUPPORT TO SHOW CURENT SONG

keyboard.modules.append(encoder)

if __name__ == "__main__":
    keyboard.go()
