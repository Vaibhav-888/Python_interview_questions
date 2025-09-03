# Multiprocessing simple example
import multiprocessing
import os


def print_cube(num):
    print(f"Cube: {num * num * num}")


def print_square(num):
    print(f"Square: {num * num}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = print_cube, args = (10, ))
    p2 = multiprocessing.Process(target = print_square, args = (10, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")

def worker1():
    print(f"ID of process of running worker1: {os.getpid()}")

def worker2():
    print(f"ID of process of running worker2: {os.getpid()}")

if __name__ == "__main__":

    print(f"ID of main process: {os.getpid()}")
    p1 = multiprocessing.Process(target = worker1)
    p2 = multiprocessing.Process(target = worker2)

    p1.start()
    p2.start()

    print(f"ID of process p1: {p1.pid}")
    print(f"ID of process p2: {p2.pid}")

    p1.join()
    p2.join()

    print("Both processes are finished execution!")

    print(f"p1 process is alive: {p1.is_alive()}")
    print(f"p2 process is alive: {p2.is_alive()}")