import asyncio
import time

# ฟังก์ชัน factorial(n) มีการใช้ await asyncio.sleep(1) เพื่อหน่วงเวลา 1 วินาที แบบ asynchronous 
# ในแต่ละรอบของลูป for ที่คำนวณ Factorial เพื่อให้โปรแกรมรอให้ Event Loop ทำงานต่อไป
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    return f
# เพื่อรวมผลลัพธ์ที่ได้จากการคำนวณ Factorial ของตัวเลข 2, 3, และ 4 ในแบบ asynchronous ให้กลายเป็น concurrent
#  และรอให้ทุก task เสร็จสิ้นพร้อมกัน โดยผลลัพธ์ที่ได้จะเป็นlist L
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) # [2, 6, 24]

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.03 sec