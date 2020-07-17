import os
import datetime
from threading import Timer, Thread

def automation():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    if hour == 7 and (minute == 12 or minute == 20 or minute == 28) and second >= 30:
        os.system('python D:/Python/Appium/Alipay/forest.py')
    t = Timer(20, automation)
    t.start()
    if hour == 7 and minute == 38:
        os.system("taskkill /F /IM node.exe")
        t.cancel()

def call_appium():
    os.system("appium")

if __name__ == "__main__":
    print("Pls check appium is started!")
    thread_list = []
    # t1 = Thread(target=call_appium)
    # t1.start()
    t2 = Thread(target=automation)
    t2.start()
    # thread_list.append(t1)
    thread_list.append(t2)
    for t in thread_list:
        t.join()