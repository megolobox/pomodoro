import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

DATA_FILE = "pomodoro_data.json"

root = tk.Tk()
root.title("番茄钟")
root.geometry("300x420")

label = tk.Label(root, text="25:00", font=("Arial", 40))
label.pack(pady=20)

mode_label = tk.Label(root, text="学习模式", font=("Arial", 12))
mode_label.pack()

pomodoro_count = 0
history = []

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        pomodoro_count = data.get("pomodoro_count", 0)
        history = data.get("history", [])

count_label = tk.Label(root, text=f"已完成：{pomodoro_count} 个番茄", font=("Arial", 12))
count_label.pack()

history_label = tk.Label(root, text="最近记录：", font=("Arial", 10), justify=tk.LEFT)
history_label.pack(pady=5)

def refresh_history():
    text = "最近记录：\n"
    for item in history[-3:]:
        text = text + item + "\n"
    history_label.config(text=text)

refresh_history()

seconds_left = 25 * 60
timer_id = None
is_running = False
is_work_mode = True

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"pomodoro_count": pomodoro_count, "history": history}, f)

def update_timer():
    global seconds_left, timer_id, is_running, is_work_mode, pomodoro_count, history
    if seconds_left > 0:
        seconds_left = seconds_left - 1
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        label.config(text=f"{minutes:02d}:{seconds:02d}")
        timer_id = root.after(1000, update_timer)
    else:
        if is_work_mode:
            pomodoro_count = pomodoro_count + 1
            now = datetime.now().strftime("%m-%d %H:%M")
            history.append(now)
            count_label.config(text=f"已完成：{pomodoro_count} 个番茄")
            refresh_history()
            save_data()
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

def reset():
    global pomodoro_count, history
    pomodoro_count = 0
    history = []
    count_label.config(text="已完成：0 个番茄")
    refresh_history()
    save_data()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="开始", command=start, font=("Arial", 14))
start_button.pack(side=tk.LEFT, padx=10)

pause_button = tk.Button(button_frame, text="暂停", command=pause, font=("Arial", 14))
pause_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(button_frame, text="重置", command=reset, font=("Arial", 14))
reset_button.pack(side=tk.LEFT, padx=10)

root.mainloop()