#superfastpython.com
#Example of wait/notify with a condition
from time import sleep
from threading import Thread
from threading import Condition

from TAP_2025.Threads.semaphore import worker


def task(condition, work_list):
    sleep(1)
    #Add data to the work list
    work_list.append(33)
    #Notify a waiting thread that the work is done
    print("Thread sending notification...")
    with condition:
        condition.notify()

def task2(work_list):
    sleep(1)
    #Add data to the work list
    work_list.append(33)
    #Notify a waiting thread that the work is done
    print("Thread sending notification...")

#Created shared semaphore
condition = Condition(1)
#Prepare the work list
work_list = list()
#Wait to be notified that the data is ready
print("Main thread waiting for data")
with condition:
    #start a new thread to perform some work
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()

    condition.wait()
print(f"Got data: {work_list}")