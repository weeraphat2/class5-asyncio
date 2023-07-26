import asyncio
import time

#สร้าง event loop async
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
#คำนวณผลรวมของlistตัวเลขและมีการนำเข้าฟังก์ชัน sleep() หน่วงเวลา1วินาที
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
#ทำงานแบบ asynchronous และรอให้การหน่วงเวลาในฟังก์ชัน sleep() เสร็จสิ้นก่อนที่ Event Loop จะทำงานต่อไป นอกจากนี้ยังสามารถระบุ task ต่างๆ ให้ทำงานพร้อมกันและรอให้ทุก task เสร็จสิ้นด้วย asyncio.wait()
start = time.time()

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
# Task A: Computing 1+2
# Time: 1.02
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.02
# Task B: Computing 3+3
# Time: 4.04
# Task B: Sum = 6

# Time: 5.05 sec