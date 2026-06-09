import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every 1000 ms (1 second)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Helvetica', 48), fg='black')
label.pack()

update_clock()
root.mainloop()
