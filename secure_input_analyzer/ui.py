import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar

class SecureInputUI:
    def __init__(self, root, keylogger_start_cb, keylogger_stop_cb, password_analyzer_cb):
        self.root = root
        self.keylogger_start_cb = keylogger_start_cb
        self.keylogger_stop_cb = keylogger_stop_cb
        self.password_analyzer_cb = password_analyzer_cb
        self.keylogger_running = False

        # Configure the main window
        self.root.title("SecureInput Analyzer")
        self.root.geometry("400x300")
        self.root.configure(bg="black")

        # --- Widgets ---
        # Password input
        self.password_label = tk.Label(root, text="Enter Password:", bg="black", fg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Analyze button
        self.analyze_button = tk.Button(root, text="Analyze Password", bg="green", fg="white", command=self.analyze_password)
        self.analyze_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(root, text="", bg="black", fg="green", font=("Helvetica", 12))
        self.result_label.pack(pady=5)
        self.feedback_label = tk.Label(root, text="", bg="black", fg="white", wraplength=350)
        self.feedback_label.pack(pady=5)

        # Keylogger control
        self.keylogger_button = tk.Button(root, text="Start Keylogger", bg="green", fg="white", command=self.toggle_keylogger)
        self.keylogger_button.pack(pady=10)

        # View logs
        self.view_logs_button = tk.Button(root, text="View Logs", bg="green", fg="white", command=self.view_logs)
        self.view_logs_button.pack(pady=5)

    def analyze_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Input Error", "Password field cannot be empty.")
            return

        score, feedback = self.password_analyzer_cb(password)
        self.result_label.config(text=f"Password Strength Score: {score}/10")
        self.feedback_label.config(text=f"Feedback: {feedback}")

    def toggle_keylogger(self):
        if not self.keylogger_running:
            self.keylogger_start_cb()
            self.keylogger_button.config(text="Stop Keylogger", bg="red")
            self.keylogger_running = True
        else:
            self.keylogger_stop_cb()
            self.keylogger_button.config(text="Start Keylogger", bg="green")
            self.keylogger_running = False

    def view_logs(self):
        log_window = Toplevel(self.root)
        log_window.title("Keystroke Logs")
        log_window.geometry("500x400")
        log_window.configure(bg="black")

        text_area = Text(log_window, wrap="word", bg="black", fg="white")
        scrollbar = Scrollbar(log_window, command=text_area.yview)
        text_area.config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        text_area.pack(expand=True, fill="both")

        try:
            with open("logs/keystrokes.txt", "r") as f:
                text_area.insert("1.0", f.read())
        except FileNotFoundError:
            text_area.insert("1.0", "No logs found.")

        text_area.config(state="disabled")

if __name__ == '__main__':
    # Example usage for testing
    def dummy_start(): print("Keylogger started.")
    def dummy_stop(): print("Keylogger stopped.")
    def dummy_analyze(p): return (5, "This is a test.")

    root = tk.Tk()
    app = SecureInputUI(root, dummy_start, dummy_stop, dummy_analyze)
    root.mainloop()
