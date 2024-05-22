import subprocess
import pyautogui
import random
import time
import tkinter as tk
from threading import Thread
import pygetwindow as gw
import sys
import string

def generate_random_character():
    return random.choice(string.ascii_lowercase + string.digits)

def random_typing_speed():
    return random.uniform(0.1, 0.3)

def type_random_characters():
    while window_open:
        char = generate_random_character()
        pyautogui.typewrite(char)
        time.sleep(random_typing_speed())

def on_closing():
    global window_open
    window_open = False
    root.destroy()
    sys.exit()

subprocess.Popen(['notepad.exe'])

time.sleep(2)

screen_width, screen_height = pyautogui.size()

notepad_window = None
for window in gw.getWindowsWithTitle('Untitled - Notepad'):
    if window.title == 'Untitled - Notepad':
        notepad_window = window
        break

if notepad_window:
    notepad_window.moveTo(0, 0)
    notepad_window.resizeTo(screen_width // 2, screen_height)

window_open = True
root = tk.Tk()

window_width = screen_width // 2
window_height = screen_height
position_top = 0
position_right = screen_width // 2
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

root.configure(bg='#2e2e2e')
frame = tk.Frame(root, bg='#3c3f41', bd=0)
frame.pack(fill='both', expand=True, padx=20, pady=20)

exit_button = tk.Button(frame, text="Exit", command=on_closing, bg="#ff4d4d", fg="white", font=("Helvetica", 18), width=20, height=2, relief="flat")
exit_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", on_closing)

typing_thread = Thread(target=type_random_characters)
typing_thread.start()

root.mainloop()
