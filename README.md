# Keylogger Program

This Python program is a basic keylogger that logs keystrokes, tracks key combinations (such as `Ctrl + C`), and saves them to a text file. It uses the `pynput` library to listen for keyboard events.

### Features:
- Logs every key pressed, including letters, numbers, and special keys.
- Detects and logs key combinations like `Ctrl + C`, `Ctrl + V`, etc.
- Saves logged keys and words to a text file (`keylog.txt`).
- Stops the keylogger when the `Esc` key or `Ctrl + Q` is pressed.

### Requirements:
- Python 3.x
- `pynput` library (can be installed via `pip install pynput`)

### How It Works:
- The program listens to all key events (key presses and releases).
- It records every keystroke, including special keys like `Space`, `Enter`, `Shift`, `Ctrl`, and `Alt`.
- When a word is typed and the `Enter` key is pressed, the word is logged to a file.
- Key combinations, such as `Ctrl + C` and `Ctrl + V`, are detected and logged.
- The program stops when `Esc` or `Ctrl + Q` is pressed.

### How to Run:
1. Clone or download the repository.
2. Install the `pynput` library using:
   ```
   pip install pynput
   ```
3. Run the `keylogger.py` script:
   ```
   python keylogger.py
   ```
4. The keystrokes will be logged in the `keylog.txt` file.

### Ethical Considerations:
This program is designed for educational purposes. Please use it responsibly and ensure you have proper permission before using it on any system. Unauthorized use of keyloggers is illegal and unethical.