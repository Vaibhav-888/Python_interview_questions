# python multithreading simple example
import threading


def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

# explanation for above example of cube and square program.
import os


def task1():
    print(f"Task1 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task: {os.getpid()}")


def task2():
    print(f"Task2 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task: {os.getpid()}")


print()

if __name__ == "__main__":
    print(f"ID of process running program task: {os.getpid()}")

    print(f"Print main thread name: {threading.current_thread().name}")
    print()

    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

# Python ThreadPool

import concurrent.futures


def worker():
    print("Worker thread running...")


pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
