import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(3)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def b():
    blocking_io()

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        # b(),
        # b(),
        asyncio.sleep(1),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")

asyncio.run(main())