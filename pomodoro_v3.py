import tkinter as tk

root = tk.Tk()
root.title("番茄钟")
root.geometry("300x200")

label = tk.Label(root, text="25:00", font=("Arial", 40))
label.pack(pady=30)

seconds_left = 25 * 60

def update_timer():
    global seconds_left
    if seconds_left > 0:
        seconds_left = seconds_left - 1
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)
    else:
        label.config(text="时间到！")

def start():
    update_timer()

button = tk.Button(root, text="开始", command=start, font=("Arial", 14))
button.pack()

root.mainloop()