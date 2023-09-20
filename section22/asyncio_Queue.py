import asyncio


async def worker1(queue):
    print('worker1 start')
    await queue.put(100)
    print('worker1 end')
    
async def worker2(queue):
    print('worker2 start')
    x = await queue.get()
    print(x)
    print('worker2 end')

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(worker1(queue), worker2(queue))

asyncio.run(main())