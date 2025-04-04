#superfastpython.com
#Example of wait/notify with a condition
from time import sleep
from random import random, randint
from threading import Thread
from threading import Condition

def task(condition, numero):
    print(f"Thread {numero} waiting ... ")
    with condition:
        condition.wait()
    value = randint(0, 10)
    sleep(value)
    print(f"Thread {numero} got value")

#Created shared condition
condition = Condition()
for i in range(3):
    worker = Thread(target=task,args=(condition,i))
    worker.start()

sleep(3)
with condition:
    condition.notify_all()