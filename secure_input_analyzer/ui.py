import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar
from tkinter import ttk

class SecureInputUI:
    def __init__(self, root, keylogger_start_cb, keylogger_stop_cb, password_analyzer_cb,
                 brute_force_estimator_cb=None, phishing_analyzer_cb=None):
        self.root = root
        self.keylogger_start_cb = keylogger_start_cb
        self.keylogger_stop_cb = keylogger_stop_cb
        self.password_analyzer_cb = password_analyzer_cb
        self.brute_force_estimator_cb = brute_force_estimator_cb
        self.phishing_analyzer_cb = phishing_analyzer_cb
        self.keylogger_running = False

        # Configure the main window
        self.root.title("SecureInput Analyzer")
        self.root.geometry("500x400")
        self.root.configure(bg="black")

        # --- Tabbed Interface ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Tab 1: Password Analyzer
        self.password_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.password_tab, text="Password Analyzer")
        self._create_password_analyzer_tab()

        # Tab 2: Brute Force Simulator
        self.brute_force_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.brute_force_tab, text="Brute Force Simulator")
        self._create_brute_force_tab()

        # Tab 3: Phishing Analyzer
        self.phishing_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.phishing_tab, text="Phishing Analyzer")
        self._create_phishing_analyzer_tab()

        # --- Keylogger and Logs ---
        # Keylogger control
        self.keylogger_button = tk.Button(root, text="Start Keylogger", bg="green", fg="white", command=self.toggle_keylogger)
        self.keylogger_button.pack(pady=5)

        # View logs
        self.view_logs_button = tk.Button(root, text="View Logs", bg="green", fg="white", command=self.view_logs)
        self.view_logs_button.pack(pady=5)

    def _create_password_analyzer_tab(self):
        # Password input
        self.password_label = tk.Label(self.password_tab, text="Enter Password:", bg="black", fg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.password_tab, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Analyze button
        self.analyze_button = tk.Button(self.password_tab, text="Analyze Password", bg="green", fg="white", command=self.analyze_password)
        self.analyze_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(self.password_tab, text="", bg="black", fg="green", font=("Helvetica", 12))
        self.result_label.pack(pady=5)
        self.feedback_label = tk.Label(self.password_tab, text="", bg="black", fg="white", wraplength=350)
        self.feedback_label.pack(pady=5)

    def _create_brute_force_tab(self):
        # Password input
        self.bf_password_label = tk.Label(self.brute_force_tab, text="Enter Password:", bg="black", fg="white")
        self.bf_password_label.pack(pady=5)
        self.bf_password_entry = tk.Entry(self.brute_force_tab, show="*", width=30)
        self.bf_password_entry.pack(pady=5)

        # Attack speed slider
        self.slider_label = tk.Label(self.brute_force_tab, text="Simulated Attempts per Second:", bg="black", fg="white")
        self.slider_label.pack(pady=5)
        self.speed_slider = tk.Scale(self.brute_force_tab, from_=1000, to=100_000_000_000, orient="horizontal", length=300)
        self.speed_slider.set(1_000_000)
        self.speed_slider.pack(pady=5)

        # Estimate button
        self.estimate_button = tk.Button(self.brute_force_tab, text="Estimate Crack Time", bg="green", fg="white", command=self.estimate_crack_time)
        self.estimate_button.pack(pady=10)

        # Result display
        self.bf_result_label = tk.Label(self.brute_force_tab, text="", bg="black", fg="green", font=("Helvetica", 12))
        self.bf_result_label.pack(pady=5)

    def _create_phishing_analyzer_tab(self):
        # Email content input
        self.phishing_label = tk.Label(self.phishing_tab, text="Paste Email Content Below:", bg="black", fg="white")
        self.phishing_label.pack(pady=5)
        self.email_text = Text(self.phishing_tab, wrap="word", height=10, width=50)
        self.email_text.pack(pady=5, padx=10)

        # Analyze button
        self.phishing_analyze_button = tk.Button(self.phishing_tab, text="Analyze Email", bg="green", fg="white", command=self.analyze_phishing_email)
        self.phishing_analyze_button.pack(pady=10)

        # Result display
        self.phishing_result_label = tk.Label(self.phishing_tab, text="", bg="black", fg="green", justify="left", wraplength=400)
        self.phishing_result_label.pack(pady=5)

    def analyze_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Input Error", "Password field cannot be empty.")
            return

        score, feedback = self.password_analyzer_cb(password)
        self.result_label.config(text=f"Password Strength Score: {score}/10")
        self.feedback_label.config(text=f"Feedback: {feedback}")

    def estimate_crack_time(self):
        password = self.bf_password_entry.get()
        if not password:
            messagebox.showwarning("Input Error", "Password field cannot be empty.")
            return

        attempts_per_second = self.speed_slider.get()
        estimated_time = self.brute_force_estimator_cb(password, attempts_per_second)
        self.bf_result_label.config(text=f"Estimated time to crack: {estimated_time}")

    def analyze_phishing_email(self):
        email_content = self.email_text.get("1.0", tk.END)
        if not email_content.strip():
            messagebox.showwarning("Input Error", "Email content cannot be empty.")
            return

        red_flags = self.phishing_analyzer_cb(email_content)
        self.phishing_result_label.config(text=f"Analysis Results:\n{red_flags}")

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
    def dummy_start(): print("Keylogger started.")
    def dummy_stop(): print("Keylogger stopped.")
    def dummy_analyze(p): return (5, "This is a test.")

    root = tk.Tk()
    app = SecureInputUI(root, dummy_start, dummy_stop, dummy_analyze)
    root.mainloop()
