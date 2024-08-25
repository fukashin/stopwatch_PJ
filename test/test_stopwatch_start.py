from app.stopwatch import StopWatch

stopwatch = StopWatch()

stopwatch.start()

if not stopwatch.is_running:
    raise Exception("startの挙動が正しくありません")

print("テストに合格しました")
