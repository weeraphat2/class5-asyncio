import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30


def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")

# อธิบายการทำงานแบบ synchonous
# แบบ synchonous Judit จะเล่นทีละเกมส์ จะไม่ย้ายไปเกมส์ถัดไปจนกว่าเกมส์ที่เล่นปัจจุบันจะจบ 
# ซึ่งเเต่ละเกมส์จะใช้เวลา ((55 + 5) * 30) = 30 นาที(1800 วินาที) ซึ่งเวลาที่ใช้ในการเล่นเกมส์ทั้งหมดจะเท่ากับ 
# 24 opponents * 30 นาที = 720 นาที หรือ 12 ชั่วโมง
