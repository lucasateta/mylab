import asyncio
# from random import random
import random
import time

'''
# Lock

An asyncio lock can be used to guarantee exclusive access to a shared resource.
'''
lock = asyncio.Lock()

async def use_lock_contextmanager():
    async with lock:
        print("a")

async def use_lock_regular():
    lock = asyncio.Lock()

    await lock.acquire()
    try:
        print("a")
    finally:
        lock.release()

asyncio.run(use_lock_contextmanager())
asyncio.run(use_lock_regular())

'''
# Event

An asyncio event can be used to notify multiple asyncio tasks that some event has happened.

An Event object manages an internal flag that can be set to true with the set() method and reset to false
with the clear() method. The wait() method blocks until the flag is set to true.
'''

async def waiter(event: asyncio.Event):
    print('waiting for it ...')
    await event.wait()
    print('... got it')

async def use_event():
    # Create an Event object
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))

    # Sleep for 1 second and set the event
    await asyncio.sleep(1)
    event.set()

    await waiter_task

asyncio.run(use_event())

'''
# Condition

An asyncio condition primitive can be used by a task tot wait for some event to happen and then get
exclusive access to a shared resource.

In essense, a Condition object combines the functionality of an Event and a Lock. It is possible to have
multiple Condition objects share one Lock, which allows coordinating exclusive access to a shred resource
between different tasks interested in particular states of that shared resource.
'''

async def use_cond_contextmanager():
    cond = asyncio.Condition()

    async def delayed_notify():
        print("delayed_notify")
        await asyncio.sleep(4)
        print("notifying...")
        async with cond:
            cond.notify_all()

    task = asyncio.create_task(delayed_notify())

    print("start waiting...")
    async with cond:
        await cond.wait()
        print("done waiting.")

    await task

async def use_cond_regular():
    cond = asyncio.Condition()
    work_list = list()

    async def task_producer(condition, work_list):
        await asyncio.sleep(1)
        work_list.append(33)
        print('Producer sending notification...')
        async with condition:
            condition.notify()

    async with cond:
        _ = asyncio.create_task(task_producer(cond, work_list))
        await cond.wait()
        print(work_list)

asyncio.run(use_cond_contextmanager())
asyncio.run(use_cond_regular())


'''
# Semaphore

A semaphore manages an internal counter which is decremented by each acquire() call and incremented
by each release() call.
'''

async def use_semaphore_contextmanager():
    # create the shared semaphore
    sem = asyncio.Semaphore(2)

    # task coroutine
    async def task(semaphore, number):
        # acquire the semaphore
        async with semaphore:
            value = random.random()
            await asyncio.sleep(value)
            print(f"Task {number} got {value}")

    async with sem:
        tasks = [asyncio.create_task(task(sem, i)) for i in range(10)]
        _ = await asyncio.wait(tasks)

asyncio.run(use_semaphore_contextmanager())


'''
# Queues
'''

async def use_queue():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # This is the worker coroutine that get work item from the queue
    async def worker(name, queue):
        while True:
            print(asyncio.get_running_loop())
            # Get a "work item" out of the queue
            sleep_for = await queue.get()

            # Sleep for the "sleep_for" seconds.
            await asyncio.sleep(sleep_for/10)

            # Notify the queue that the "work item" has been processed.
            queue.task_done()
            
            print(f"{name} has slept for {sleep_for/10:.2f} seconds")

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()

    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print(f"3 workers slept in parallel for {total_slept_for: .2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds")

asyncio.run(use_queue())

''''
Event Loop
'''

def hello_world(loop: asyncio.AbstractEventLoop):
    print('Hello world')
    loop.stop()

loop = asyncio.new_event_loop()
loop.call_soon(hello_world, loop)

try:
    loop.run_forever()
finally:
    loop.close()

'''
Futures
'''

async def use_future():
    async def set_after(fut, delay, value):
        # Sleep for *delay* seconds
        await asyncio.sleep(delay)

        # Set *value* as a result of *fut* Future.
        fut.set_result(value)

    loop = asyncio.get_running_loop()

    # Create a new Future object
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # We already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(set_after(fut, 1, '...world'))
    print('Hello...')

    print(await fut)

asyncio.run(use_future())