from app.stopwatch import StopWatch

stopwatch = StopWatch()

stopwatch.elapsed_time = 100
if stopwatch.get_display_time() != "00:00:00.10":
    raise Exception("get_display_timeの挙動が正しくありません")

stopwatch.elapsed_time = 1000
if stopwatch.get_display_time() != "00:00:01.00":
    raise Exception("get_display_timeの挙動が正しくありません")

stopwatch.elapsed_time = 100000
if stopwatch.get_display_time() != "00:01:40.00":
    raise Exception("get_display_timeの挙動が正しくありません")

stopwatch.elapsed_time = 10000000
if stopwatch.get_display_time() != "02:46:40.00":
    raise Exception("get_display_timeの挙動が正しくありません")

print("テストに合格しました")
