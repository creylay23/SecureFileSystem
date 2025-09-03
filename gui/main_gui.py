
import tkinter as tk
from tkinter import messagebox

def send_message():
    message = entry.get()
    messagebox.showinfo("Message Sent", f"You entered: {message}")

root = tk.Tk()
root.title("Secure Message Sender")
root.geometry("300x150")

label = tk.Label(root, text="Enter your message:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=10)

root.mainloop()