from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

kbd = KeyboardController()
mse = MouseController()

time.sleep(2)
mse.click(Button.left, 1)
# kbd.press(Key.esc)
# time.sleep(0.01)
# kbd.release(Key.esc)

# time.sleep(0.01)
# kbd.press(Key.esc)
# time.sleep(0.01)
# kbd.release(Key.esc)
