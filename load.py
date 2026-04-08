import tkinter as tk
from tkinter import simpledialog
import keyboard

root = tk.Tk()


root.attributes("-topmost", True)
root.overrideredirect(True) 
root.geometry("800x600+100+100") 
root.configure(bg="black")
root.wm_attributes("-transparentcolor", "black")

label = tk.Label(
    root,
    text="",
    font=("Arial", 80, "bold"),
    fg="green",
    bg="black"
)
label.pack(expand=True)

# --- FUNCTIONS ---
def set_message(text, color):
    label.config(text=text, fg=color)


def show_warning():
    root.after(0, set_message, "STOP TALKING", "red")

def good_job():
    root.after(0, set_message, "Well Done!", "green")

def shh_warn():
    root.after(0, set_message, "Shh! Quiet time!", "yellow") 

def custom_message():
    message = simpledialog.askstring("Message", "Enter message:", parent=root)
    color = simpledialog.askstring("Color", "Enter color:", parent=root)
    if message and color:
        root.after(0, set_message, message, color)

def hide_warning():
    root.after(0, set_message, "", "green")

def move_mode():
    """Temporary visible window for dragging."""
    root.overrideredirect(False)
    root.configure(bg="gray")
    root.wm_attributes("-transparentcolor", "") 

def lock_mode():
    """Go back to transparent overlay."""
    root.overrideredirect(True)  
    root.configure(bg="black") 
    root.wm_attributes("-transparentcolor", "black")

def kill() -> None:
    """Cleanly exit the application."""
    root.destroy()

# --- HOTKEYS ---
keyboard.add_hotkey("F9", show_warning)
keyboard.add_hotkey("F8", good_job)
keyboard.add_hotkey("F7", shh_warn)
keyboard.add_hotkey("F10", hide_warning)
keyboard.add_hotkey("F6", move_mode)
keyboard.add_hotkey("F5", lock_mode) 
keyboard.add_hotkey("F4", custom_message) 
keyboard.add_hotkey("F3", kill)  

print("F7 = shh warning")
print("F8 = good job")
print("F5 = lock overlay")
print("F6 = move window")
print("F9 = show warning")
print("F10 = hide message")
print("F4 = custom message input")

root.mainloop()
