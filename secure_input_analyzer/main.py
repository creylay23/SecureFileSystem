import tkinter as tk
from keylogger import Keylogger
from password_checker import PasswordChecker
from ui import SecureInputUI

def main():
    # Instantiate the backend modules
    keylogger = Keylogger()
    password_checker = PasswordChecker()

    # Create the main Tkinter window
    root = tk.Tk()

    # Instantiate the UI, passing the backend methods as callbacks
    app = SecureInputUI(
        root,
        keylogger_start_cb=keylogger.start,
        keylogger_stop_cb=keylogger.stop,
        password_analyzer_cb=password_checker.analyze
    )

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
