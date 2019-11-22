import asyncio
import time

test_ls = [1,2,3,4,5]

async def test_no_async():
	for item in test_ls:
		print(item)
		await asyncio.sleep(0)
async def test_no_async1():
	print('waited 1 secs')


async def main():
	print('wat')
	async0 = loop1.create_task(test_no_async())
	async1 = loop1.create_task(test_no_async1())
	#print(short_task)

asyncio.run(main())