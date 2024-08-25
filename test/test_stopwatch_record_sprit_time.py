from app.stopwatch import StopWatch

stopwatch = StopWatch()

stopwatch.elapsed_time = 100
stopwatch.record_split_time()

if stopwatch.split_time[-1] != 100:
    raise Exception("record_split_timeの挙動が正しくありません")

stopwatch.elapsed_time = 1000
stopwatch.record_split_time()

if stopwatch.split_time[-1] != 1000:
    raise Exception("record_split_timeの挙動が正しくありません")

print("テストに合格しました")