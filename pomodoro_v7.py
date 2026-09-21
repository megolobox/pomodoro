import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("番茄钟")
root.geometry("300x280")

label = tk.Label(root, text="25:00", font=("Arial", 40))
label.pack(pady=20)

mode_label = tk.Label(root, text="学习模式", font=("Arial", 12))
mode_label.pack()

count_label = tk.Label(root, text="已完成：0 个番茄", font=("Arial", 12))
count_label.pack()

seconds_left = 25 * 60
timer_id = None
is_running = False
is_work_mode = True
pomodoro_count = 0

def update_timer():
    global seconds_left, timer_id, is_running, is_work_mode, pomodoro_count
    if seconds_left > 0:
        seconds_left = seconds_left - 1
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        label.config(text=f"{minutes:02d}:{seconds:02d}")
        timer_id = root.after(1000, update_timer)
    else:
        if is_work_mode:
            pomodoro_count = pomodoro_count + 1
            count_label.config(text=f"已完成：{pomodoro_count} 个番茄")
            messagebox.showinfo("番茄钟", "25分钟学习结束，休息5分钟！")
            is_work_mode = False
            mode_label.config(text="休息模式")
            seconds_left = 5 * 60
        else:
            messagebox.showinfo("番茄钟", "5分钟休息结束，继续学习！")
            is_work_mode = True
            mode_label.config(text="学习模式")
            seconds_left = 25 * 60 
        label.config(text=f"{seconds_left // 60:02d}:{seconds_left % 60:02d}")
        timer_id = root.after(1000, update_timer)

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
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="开始", command=start, font=("Arial", 14))
start_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(button_frame, text="暂停", command=pause, font=("Arial", 14))
pause_button.pack(side=tk.LEFT, padx=10)

root.mainloop()