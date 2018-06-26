import asyncio

async def compute(future):
  print("Tell me...")

  # Simulate IO
  res = await answer()

  print("NOW!!!")

  future.set_result(res)

async def answer():
  print('calculating')
  await asyncio.sleep(2)
  return 42

f = asyncio.Future()
loop = asyncio.get_event_loop()
loop.run_until_complete(compute(f))
loop.close()
f.result()