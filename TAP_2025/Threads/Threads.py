
"""
Hilos en python
"""

import time
from threading import Thread, current_thread

def task1():
    time.sleep(2)
    print(f"Soy {current_thread().name} y he terminado la tarea 1 ...")

def task2():
    time.sleep(3)
    print(f"soy {current_thread().name} y he terminado la tarea 2 ...")

#task1()
#task2()

print(f"soy {current_thread().name} ")
hilo1 = Thread(target=task1)
hilo2 = Thread(target=task2)
ti = time.time()
hilo1.start()
hilo2.start()

#Investigar que es hace el metodo .join()
hilo2.join()
hilo1.join()
tf = time.time()

print(f"duración: {tf-ti}")

print("Todos los hilos se han ejecutado")