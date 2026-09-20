import tkinter as tk

root = tk.Tk()
root.title("番茄钟")
root.geometry("300x200")

label = tk.Label(root, text="25:00", font=("Arial", 40))
label.pack(pady=30)

seconds_left = 25 * 60
timer_id = None
is_running = False

def update_timer():
    global seconds_left, timer_id, is_running
    if seconds_left > 0:
        seconds_left = seconds_left - 1
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        label.config(text=f"{minutes:02d}:{seconds:02d}")
        timer_id = root.after(1000, update_timer)
    else:
        label.config(text="时间到！")
        is_running = False

def start():
    global is_running
    if not is_running:
        is_running = True
        update_timer()

def pause():
    global is_running, timer_id
    if is_running:
        is_running = False
        if timer_id:
            root.after_cancel(timer_id)
            timer_id = None

button_frame = tk.Frame(root)
button_frame.pack()

start_button = tk.Button(button_frame, text="开始", command=start, font=("Arial", 14))
start_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(button_frame, text="暂停", command=pause, font=("Arial", 14))
pause_button.pack(side=tk.LEFT, padx=10)

root.mainloop()