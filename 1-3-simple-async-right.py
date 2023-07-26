import asyncio
import time

async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)
#โดยการใช้ await asyncio.sleep(1) ในฟังก์ชัน sleep() จะทำให้โปรแกรมทำงานแบบ asynchronous และสามารถรอให้ Event Loop ทำงานต่อไปได้ 
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#สร้าง event loop
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3]))
]
#run event loop โดยใช้ loop.run_until_complete
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')

# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.03
# Task B: Sum = 6

# Time: 3.03 sec