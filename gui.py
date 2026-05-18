import tkinter as tk
from tkinter import messagebox
import subprocess
import shutil

# =========================
# Window
# =========================

root = tk.Tk()
root.title("Traffic")
root.geometry("500x400")
root.configure(bg="#1e1e1e")
root.minsize(400, 300)

# =========================
# Log Function
# =========================

def log(message):

    output_box.config(state="normal")

    output_box.insert(tk.END, message + "\n")

    output_box.config(state="disabled")

    output_box.see(tk.END)

# =========================
# Title / Logo
# =========================

title = tk.Label(
    root,
    text="Traffic v2.0",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

try:

    logo = tk.PhotoImage(file="assets/logo.png")

    logo_label = tk.Label(
        root,
        image=logo,
        bg="#1e1e1e"
    )

    logo_label.pack(pady=10)

except Exception as e:

    log(f"Logo loading failed: {e}")

# =========================
# PID Entry
# =========================

pid_label = tk.Label(
    root,
    text="Process PID:",
    bg="#1e1e1e",
    fg="white"
)

pid_label.pack()

pid_entry = tk.Entry(
    root,
    width=30
)

pid_entry.pack(pady=5)

# =========================
# Signal Entry
# =========================

signal_label = tk.Label(
    root,
    text="Signal:",
    bg="#1e1e1e",
    fg="white"
)

signal_label.pack()

signal_entry = tk.Entry(
    root,
    width=30
)

signal_entry.pack(pady=5)

# =========================
# Output box
# =========================

output_box = tk.Text(
    root,
    height=8,
    width=50,
    bg="#2b2b2b",
    fg="white"
)

output_box.pack(pady=15)

# =========================
# Functions
# =========================

def send_signal():
    pid = pid_entry.get()
    signal = signal_entry.get()

    # Confirmation
    if signal == "9":
        output_box.insert(tk.END, f"[Kill Confirmation] You are about to send SIGKILL to {pid} !")


    output_box.insert(tk.END, f"Sending {signal} to PID {pid}...\n")

    try:
        result = subprocess.run(
            ["./traffic", "signal", pid, signal],
            capture_output=True,
            text=True,
            check=True
        )

        log(result.stdout)


    except Exception as e:
        output_box.insert(tk.END, f"Error: {e}\n")


def create_process():

    log("Creating test process...")

    # =========================
    # Find a safe application
    # =========================

    app = None

    if shutil.which("kwrite"):
        app = "kwrite"

    elif shutil.which("gedit"):
        app = "gedit"

    elif shutil.which("xterm"):
        app = "xterm"

    else:
        log("No suitable GUI app found (kwrite/gedit/xterm missing).")
        return

    try:
        process = subprocess.Popen(
            [app],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )

        pid = process.pid

        log(f"Process launched: {app}")
        log(f"PID: {pid}")

    except Exception as e:
        log(f"Failed to launch process: {e}")


def exit_app():
    root.destroy()

# =========================
# Buttons
# =========================

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

signal_button = tk.Button(
    button_frame,
    text="Send Signal",
    command=send_signal,
    width=15
)

signal_button.grid(row=0, column=0, padx=5)

process_button = tk.Button(
    button_frame,
    text="New Test Process",
    command=create_process,
    width=15
)

process_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    command=exit_app,
    width=15
)

exit_button.grid(row=0, column=2, padx=5)

# =========================
# Start app
# =========================

root.mainloop()