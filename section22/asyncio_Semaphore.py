import asyncio


async def worker1(semaphore):
    async with semaphore:
        print('worker1 start')
        await asyncio.sleep(3)
        print('worker1 end')
    
async def worker2(semaphore):
    async with semaphore:
        print('worker2 start')
        await asyncio.sleep(3)
        print('worker2 end')

async def main():
    semaphore = asyncio.Semaphore(1)
    await asyncio.gather(worker1(semaphore), worker2(semaphore))

asyncio.run(main())