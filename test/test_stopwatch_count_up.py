from app.stopwatch import StopWatch
import time
import threading

stopwatch = StopWatch()


def check_count_up(stopwatch, elapsed_time, count_up_time):
    stopwatch.elapsed_time = elapsed_time
    stopwatch.is_running = True
    thread = threading.Thread(target=stopwatch.count_up)
    thread.start()
    time.sleep(count_up_time)
    stopwatch.is_running = False
    thread.join()
    base_time = (count_up_time + elapsed_time) * 1000
    is_exception = False
    if elapsed_time == 359999999:
        if not stopwatch.elapsed_time <= 359999999:
            is_exception = True
    elif not ((base_time - 10) <= stopwatch.elapsed_time <= base_time):
        is_exception = True
    if is_exception:
        raise Exception(f"count_upの挙動が正しくありません。count_up_time:{count_up_time}, elapsed_time:{stopwatch.elapsed_time}")
    stopwatch.elapsed_time = 0


check_count_up(stopwatch, 0, 1)
check_count_up(stopwatch, 0, 3)
check_count_up(stopwatch, 0, 10)
check_count_up(stopwatch, 359999999, 1)

print("テストに合格しました")
