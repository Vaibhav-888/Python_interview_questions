"""
Synchronous: Means tasks are performed one after another. Each task must complete before the next
one starts. This is simple but can block the program if a task takes a long time, like waiting
for I/O or a network call

Asynchronous: Allows tasks to run independantly without waiting for other tasks finish. While
one task is waiting (for example, on I/O), another can execute. In python, this is usually
implemented using async/await, asyncio, or frameworks like FastAPI for non-blocking requests.
"""

# synchrous example
import time

def task(name):
    t = time.sleep(2)
    print(f"Task {name} done!")

task("a")
task("b")

# asynchronous example
import asyncio

async def task(name):
    await asyncio.sleep(2)
    print(f"Task {name} complete!")

async def main():
    await asyncio.gather(task("a"), task("b"))

asyncio.run(main())