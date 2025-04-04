#superfastpython.com
#Example of wait/notify with a condition
from time import sleep
from random import random
from threading import Thread
from threading import Condition

def task(condition, work_list):
    value = (random())*10
    sleep(value)
    with condition:
        value = random()
        sleep(value)
        work_list.append(value)
        print(f"Thread added {value}")
        condition.notify()

#Created shared condition
condition = Condition()
work_list = list()
for i in range(20):
    worker = Thread(target=task,args=(condition,work_list))
    worker.start()

sleep(3)
with condition:
    condition.wait_for(lambda : len(work_list) >= 1)
    print(f"Done, got {work_list}")