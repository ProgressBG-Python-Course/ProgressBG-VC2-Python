import asyncio

async def couroutineA():
  # simulate i/o operation using sleep
  await asyncio.sleep(5)
  print("Welcome")


async def couroutineB():
  print("May I come in?")
  await couroutineA()
  print("NO, I WILL NOT WAIT!")



loop = asyncio.get_event_loop()
couroutineA_worker = couroutineA()
couroutineB_worker = couroutineB()

loop.run_until_complete(asyncio.gather(couroutineA_worker, couroutineB_worker))
loop.close()