import asyncio


async def long_task_1():
    await asyncio.sleep(3)
    print("task 1 done")


async def long_task_2():
    await asyncio.sleep(2)
    print("task 2 done")


async def async_main():
    task1 = asyncio.create_task(long_task_1())
    task2 = asyncio.create_task(long_task_2())

    await task1
    await task2


def main():
    asyncio.run(async_main())
