import asyncio
import time

#สร้าง event การทำงาน hello(1) และ hello(2) ทั้งสองงานทำงานพร้อมกัน 
#ให้ฟังก์ชันmain() รัน await task1 และ await task2 แทนการใช้ asyncio.gather

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately, the task is created
    #await asyncio.sleep
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

# Wed Jul 26 15:05:49 2023 hello 1 started
# Wed Jul 26 15:05:49 2023 hello 2 started
# Wed Jul 26 15:05:53 2023 hello 1 done
# Wed Jul 26 15:05:53 2023 hello 2 done
# Time: 4.02 sec