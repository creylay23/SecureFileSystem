import tkinter as tk
from keylogger import Keylogger
from password_checker import PasswordChecker
from brute_force_simulator import BruteForceSimulator
from phishing_analyzer import PhishingAnalyzer
from ui import SecureInputUI

def main():
    # Instantiate the backend modules
    keylogger = Keylogger()
    password_checker = PasswordChecker()
    brute_force_simulator = BruteForceSimulator()
    phishing_analyzer = PhishingAnalyzer()

    # Create the main Tkinter window
    root = tk.Tk()

    # Instantiate the UI, passing the backend methods as callbacks
    app = SecureInputUI(
        root,
        keylogger_start_cb=keylogger.start,
        keylogger_stop_cb=keylogger.stop,
        password_analyzer_cb=password_checker.analyze,
        brute_force_estimator_cb=brute_force_simulator.estimate_crack_time,
        phishing_analyzer_cb=phishing_analyzer.analyze_email
    )

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
