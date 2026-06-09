import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")

clock_label = tk.Label(
    root,
    font=("Arial", 40),
    text="",
)
clock_label.pack(expand=True)

update_time()
root.mainloop()