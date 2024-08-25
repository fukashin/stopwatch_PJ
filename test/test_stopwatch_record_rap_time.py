from app.stopwatch import StopWatch

stopwatch = StopWatch()

stopwatch.split_time = [100]
stopwatch.record_rap_time()

if stopwatch.rap_time[-1] != 100:
    raise Exception("record_rap_timeの挙動が正しくありません")

stopwatch.split_time = [100, 1000]
stopwatch.record_rap_time()

if stopwatch.rap_time[-1] != (stopwatch.split_time[-1] - stopwatch.split_time[-2]):
    raise Exception("record_rap_timeの挙動が正しくありません")

stopwatch.split_time.clear()
check_exception: bool

try:
    stopwatch.record_rap_time()
    check_exception = True
except:
    check_exception = False

if check_exception:
    raise Exception("record_rap_timeの挙動が正しくありません")

print("テストに合格しました")
