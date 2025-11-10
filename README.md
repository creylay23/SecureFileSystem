# SecureInput Analyzer

## Objective
SecureInput Analyzer is a Python desktop application designed to ethically simulate keylogging and analyze password strength. The app's primary goal is to educate users on password vulnerabilities and promote stronger security habits.

## Features
- **Keylogger Module:** A local, ethical keylogger to demonstrate how keystrokes can be captured.
- **Password Strength Checker:** Analyzes passwords based on entropy, dictionary checks, and common patterns.
- **GUI Interface:** A sleek and simple user interface with a green, white, and black theme.
- **Real-time Feedback:** Provides a score from 1-10 and textual feedback on password strength.
- **Log File Storage:** Captured keystrokes are stored locally in `logs/keystrokes.txt`.

## Ethical Disclaimer
This tool is for educational purposes only. The keylogger is intended for local use on your own machine to understand how such tools work. Do not use this tool on any computer you do not own or have explicit permission to monitor. The developers are not responsible for any misuse of this software.

## Tech Stack
- Python 3.x
- Tkinter (for the GUI)
- pynput (for the keylogger)

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SecureInput-Analyzer
   ```

2. **Install the required packages:**
   ```bash
   pip install pynput
   ```

3. **Run the application:**
   ```bash
   python secure_input_analyzer/main.py
   ```

## How to Use
1. **Launch the application.**
2. **Start the Keylogger:** Click the "Start Keylogger" button to begin capturing keystrokes. The button will turn red, indicating that the keylogger is active.
3. **Analyze a Password:** Enter a password in the input field and click "Analyze Password." The application will display a strength score and provide feedback.
4. **Stop the Keylogger:** Click the "Stop Keylogger" button to stop capturing keystrokes.
5. **View Logs:** Click the "View Logs" button to see the captured keystrokes in a new window.
