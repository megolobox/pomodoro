import tkinter as tk

root = tk.Tk()
root.title("番茄钟")
root.geometry("300x200")

label = tk.Label(root, text="25:00", font=("Arial", 40))
label.pack(pady=30)

def start():
    label.config(text="开始计时...")

button = tk.Button(root, text="开始", command=start, font=("Arial", 14))
button.pack()

root.mainloop()