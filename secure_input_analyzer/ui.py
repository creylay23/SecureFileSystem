import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from password_checker import check_strength, estimate_crack_time, is_dictionary_word
from keylogger import start_keylogger, stop_keylogger, read_log, clear_log, on_press


def log_password_key(event):
    try:
        on_press(event)
    except Exception:
        pass


class SecureInputApp:
    def __init__(self, root):
        self.sim_result = None
        self.sim_entry = None
        self.refresh_status = None
        self.log_display = None
        self.result_label = None
        self.pwd_entry = None
        self.root = root
        self.root.title("SecureInput Analyzer")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.show_splash()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook", background="black", borderwidth=0)
        style.configure("TNotebook.Tab", background="green", foreground="white", font=("Arial", 12))
        style.map("TNotebook.Tab", background=[("selected", "black")], foreground=[("selected", "green")])

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(expand=1, fill="both")

        self.create_password_tab()
        self.create_keylogger_tab()
        self.create_simulation_tab()

        start_keylogger()

    def show_splash(self):
        splash = tk.Toplevel(self.root)
        splash.title("Welcome")
        splash.geometry("400x200")
        splash.configure(bg="black")
        tk.Label(splash, text="Welcome to SecureInput Analyzer", fg="green", bg="black", font=("Arial", 16)).pack(pady=40)
        tk.Label(splash, text="Built for cybersecurity education", fg="white", bg="black", font=("Arial", 12)).pack()
        splash.after(3000, splash.destroy)

    def create_password_tab(self):
        tab = tk.Frame(self.tabs, bg="black")
        self.tabs.add(tab, text="Password Checker")

        tk.Label(tab, text="Enter Password:", fg="white", bg="black", font=("Arial", 14)).pack(pady=10)
        self.pwd_entry = tk.Entry(tab, show="*", width=40, font=("Arial", 14))
        self.pwd_entry.pack()
        self.pwd_entry.bind("<Key>", log_password_key)

        tk.Button(tab, text="Analyze", command=self.analyze_password, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)
        self.result_label = tk.Label(tab, text="", fg="green", bg="black", font=("Arial", 12))
        self.result_label.pack()

        tk.Button(tab, text="Export Report", command=self.export_report, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

    def analyze_password(self):
        pwd = self.pwd_entry.get()
        strength, entropy = check_strength(pwd)
        crack_time = estimate_crack_time(entropy)
        dictionary_flag = is_dictionary_word(pwd)
        warning = "⚠️ Common dictionary word!" if dictionary_flag else ""
        self.result_label.config(text=f"Strength: {strength}\nEntropy: {entropy}\nCrack Time: {crack_time}\n{warning}")

    def export_report(self):
        pwd = self.pwd_entry.get()
        strength, entropy = check_strength(pwd)
        crack_time = estimate_crack_time(entropy)
        dictionary_flag = is_dictionary_word(pwd)
        warning = "Common dictionary word!" if dictionary_flag else "No dictionary match."

        with open("logs/password_report.md", "w") as f:
            f.write(f"# Password Analysis Report\n\n")
            f.write(f"**Password:** {pwd}\n")
            f.write(f"**Strength:** {strength}\n")
            f.write(f"**Entropy:** {entropy}\n")
            f.write(f"**Estimated Crack Time:** {crack_time}\n")
            f.write(f"**Dictionary Match:** {warning}\n")

        messagebox.showinfo("Export Complete", "Report saved to logs/password_report.md")

    def create_keylogger_tab(self):
        tab = tk.Frame(self.tabs, bg="black")
        self.tabs.add(tab, text="Keylogger Demo")

        self.log_display = scrolledtext.ScrolledText(tab, width=90, height=20, bg="black", fg="white", font=("Courier", 12))
        self.log_display.pack(pady=10)

        btn_frame = tk.Frame(tab, bg="black")
        btn_frame.pack()

        tk.Button(btn_frame, text="Start Keylogger", command=start_keylogger, bg="green", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Stop Keylogger", command=stop_keylogger, bg="green", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Refresh Log", command=self.refresh_log, bg="green", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Clear Log", command=self.clear_log, bg="green", fg="white", font=("Arial", 12)).pack(side="left", padx=10)

        self.refresh_status = tk.Label(tab, text="", fg="green", bg="black", font=("Arial", 12))
        self.refresh_status.pack()

    def refresh_log(self):
        self.log_display.delete(1.0, tk.END)
        log_content = read_log()
        self.log_display.insert(tk.END, log_content)
        self.refresh_status.config(text="Log refreshed.")

    def clear_log(self):
        clear_log()
        self.log_display.delete(1.0, tk.END)
        self.refresh_status.config(text="Log cleared.")

    def create_simulation_tab(self):
        tab = tk.Frame(self.tabs, bg="black")
        self.tabs.add(tab, text="Security Simulation")

        tk.Label(tab, text="Enter Password to Simulate Attack:", fg="white", bg="black", font=("Arial", 14)).pack(
            pady=10)
        self.sim_entry = tk.Entry(tab, show="*", width=40, font=("Arial", 14))
        self.sim_entry.pack()

        tk.Button(tab, text="Simulate", command=self.simulate_attack, bg="green", fg="white", font=("Arial", 12)).pack(
            pady=10)
        self.sim_result = tk.Label(tab, text="", fg="green", bg="black", font=("Arial", 12))
        self.sim_result.pack()

    def simulate_attack(self):
        pwd = self.sim_entry.get()
        strength, entropy = check_strength(pwd)
        crack_time = estimate_crack_time(entropy)
        dictionary_flag = is_dictionary_word(pwd)
        warning = "⚠️ Common dictionary word!" if dictionary_flag else ""
        self.sim_result.config(
            text=f"Simulated Attack:\nStrength: {strength}\nEstimated Crack Time: {crack_time}\n{warning}")

