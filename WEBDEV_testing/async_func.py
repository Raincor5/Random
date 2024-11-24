import asyncio

async def time_consuming_task():
    print("Task started!")
    await asyncio.sleep(2)
    print("Task completed!")

asyncio.run(time_consuming_task())