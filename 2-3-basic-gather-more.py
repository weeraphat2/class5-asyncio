import asyncio
import time

# ใช้ asyncio เพื่อสร้างและรันตัวอย่างฟังก์ชัน hello(i) ในแบบ asynchronous 
# และรวมการทำงานของฟังก์ชันเหล่านั้นด้วย asyncio.gather() เพื่อรอให้ทุกฟังก์ชันเสร็จสิ้นและทำงานพร้อมกันในขณะเดียวกัน
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")
# ฟังก์ชัน main() มีการรวมการทำงานของตัวอย่างฟังก์ชัน hello(i) ด้วย await asyncio.gather(*coros)
#  เพื่อรอให้ทุกตัวอย่างฟังก์ชันเสร็จสิ้นและทำงานพร้อมกันในขณะเดียวกัน
async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

if __name__ == '_main_':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')