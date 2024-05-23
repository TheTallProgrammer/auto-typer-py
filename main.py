import subprocess
import pyautogui
import random
import time
import tkinter as tk
from threading import Thread
from ttkthemes import ThemedTk
from tkinter import ttk
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

# Set new window dimensions to stack on top of each other on the left side of the screen
window_width = screen_width // 2
window_height = screen_height // 2

notepad_window = None
for window in gw.getWindowsWithTitle('Untitled - Notepad'):
    if window.title == 'Untitled - Notepad':
        notepad_window = window
        break

if notepad_window:
    notepad_window.moveTo(0, 0)
    notepad_window.resizeTo(window_width, window_height)

window_open = True

# Use ThemedTk for a modern look
root = ThemedTk(theme='sun-valley')

# Position the Tkinter window below the Notepad window
position_top = window_height
position_left = 0
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

frame = ttk.Frame(root)
frame.pack(fill='both', expand=True, padx=20, pady=20)

# Adjust button style for better visibility and size
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 18), padding=[10, 10], width=20)

exit_button = ttk.Button(frame, text="Exit", command=on_closing, style='TButton')
exit_button.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", on_closing)

typing_thread = Thread(target=type_random_characters)
typing_thread.start()

root.mainloop()
