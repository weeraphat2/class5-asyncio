import asyncio
import time

#ใช้ async/await และ asyncio เป็นevent loop
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing = {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

#สร้าง loop async ฟังก์ชัน main เพื่อผลรวมที่ต้องทำพร้อมกันโดยใช้ await asyncio.gather
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__=='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

# Task A: Computing = 0+1
# Time: 0.00
# Task B: Computing = 0+1
# Time: 0.00
# Task A: Computing = 1+2
# Time: 1.01
# Task B: Computing = 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing = 3+3
# Time: 2.03
# Task B: Sum = 6

# Time: 3.04 sec