# 1-1-simple-sync.py
import time 

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

#คำนวณผลรวมของlistตัวเลขและมีการนำเข้าฟังก์ชัน sleep()
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    #คำนวณผลรวมของตัวเลขในlist numbers และแสดงผลการคำนวณดังกล่าว และหน่วงเวลา 1 วินาทีโดยใช้ฟังก์ชัน sleep() ก่อนที่จะเพิ่มค่าเข้าไปในตัวแปร total
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#คำนวณผลรวมของตัวเลขที่อยู่ใน list numbers
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')