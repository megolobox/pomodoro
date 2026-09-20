import time

minutes = 25
seconds = minutes * 60

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds = seconds - 1

print("时间到！")