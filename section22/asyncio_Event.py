import asyncio

async def worker1(event):
    print('worker1 start')
    await event.wait()
    print('worker1 got event')
    await asyncio.sleep(3)
    print('worker1 end')
    
async def worker2(event):
    print('worker2 start')
    await event.wait()
    print('worker2 got event')
    await asyncio.sleep(3)
    print('worker2 end')
    
async def worker3(event):
    print('worker3 start')
    print('worker3 got event')
    await asyncio.sleep(3)
    print('worker3 end')
    event.set()

async def main():
    event = asyncio.Event()
    await asyncio.gather(worker1(event), worker2(event), worker3(event))

asyncio.run(main())