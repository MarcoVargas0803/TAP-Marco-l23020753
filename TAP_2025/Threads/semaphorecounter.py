from platform import release
from random import random
from time import sleep
from threading import Thread
from threading import Semaphore

def task(counter):
    for i in range(10):
        sleep(random())
        counter.release()
        print(counter._value)

#Created shared semaphore
counter = Semaphore(2)
#Configure threads
threads = [Thread(target=task, args=(counter, ))for _ in range (1000)]
#Start threads
for thread in threads:
    thread.start()
#Wait for threads to terminate
for thread in threads:
    thread.join()
print(f"counter value: {counter._value}")

