from app.stopwatch import StopWatch

stopwatch = StopWatch()

loop_counter = 1000
for i in range(loop_counter):
    stopwatch.count_up()
if stopwatch.elapsed_time != loop_counter or stopwatch.display_time != "00:00:01.00":
    raise Exception("count_upの挙動が正しくありません")

loop_counter = 100000 - stopwatch.elapsed_time
for i in range(loop_counter):
    stopwatch.count_up()
if stopwatch.elapsed_time != 100000 or stopwatch.display_time != "00:01:40.00":
    raise Exception("count_upの挙動が正しくありません")

loop_counter = 10000000 - stopwatch.elapsed_time
for i in range(loop_counter):
    stopwatch.count_up()
if stopwatch.elapsed_time != 10000000 or stopwatch.display_time != "02:46:40.00":
    raise Exception("count_upの挙動が正しくありません")

stopwatch.elapsed_time = 359999999
stopwatch.display_time = "99:59:59.99"
stopwatch.count_up()
if stopwatch.elapsed_time != 359999999 or stopwatch.display_time != "99:59:59.99":
    raise Exception("count_upの挙動が正しくありません")

print("テストに合格しました")
