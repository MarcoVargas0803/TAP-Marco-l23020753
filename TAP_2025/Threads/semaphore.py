from random import random
from threading import Thread
from threading import Semaphore
from time import sleep


#Target function
def task(semaphore, number):
    # attempt to acquire the semaphore
    with semaphore:
        #proccess
        value = random()*10
        sleep(value)
        #report value
        print(f"Thread {number} got {value}")

#create a semaphore
semaphore = Semaphore(2)
#Create a suite of threads
for i in range(10):
    worker = Thread(target=task,args=(semaphore, i))
    worker.start()
#Wait for all workers to start