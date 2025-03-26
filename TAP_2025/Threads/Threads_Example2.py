import concurrent.futures
import logging
import threading
import time
"""
El threadingPoolExecutor es adecuado cuando queremos a varios hilos trabajando en una misma tarea.

Actividad: 
Crear un 
"""

def thread_function(name):
    logging.info(f"Thread %s: starting {threading.current_thread()}", name)
    time.sleep(2)
    logging.info(f"Thread %s: finishing{threading.current_thread()}", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    #Tamaño de pull de hilos = 3
    #Tamaño de hilos totales = 4 contando al MainThread

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))

    """threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)"""