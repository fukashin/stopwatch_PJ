from app.stopwatch import StopWatch

stopwatch = StopWatch()

stopwatch.is_running = True
stopwatch.stop()

if stopwatch.is_running:
    raise Exception("stopの挙動が正しくありません")

print("テストに合格しました")
