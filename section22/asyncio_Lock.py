import asyncio

async def worker1(lock):
    print('worker1 start')
    async with lock:
        print('worker1 got lock')
        await asyncio.sleep(3)
    print('worker1 end')
    
async def worker2(lock):
    print('worker2 start')
    async with lock:
        print('worker2 got lock')
        await asyncio.sleep(3)
    print('worker2 end')

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(worker1(lock), worker2(lock))

asyncio.run(main())