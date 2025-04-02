#superfastpython.com
#Example of a semaphore acting as a mutex
from random import random
from time import sleep
from threading import Thread, Semaphore

def task(semaphore, identifier):
    with semaphore:
        #Complete task
        print(f"Thread {identifier} working")
        sleep(random())

#Created shared semaphore
semaphore = Semaphore(1)
#Configure threads
threads = [Thread(target=task, args=(semaphore,1))for i in range (10)]
#Start threads
for thread in threads:
    thread.start()
#Wait for threads to terminate
for thread in threads:
    thread.join()

