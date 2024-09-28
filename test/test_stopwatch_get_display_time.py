from app.stopwatch import StopWatch

stopwatch = StopWatch()

if stopwatch.get_display_time(100) != ["00:00:00", ".10"]:
    raise Exception("get_display_timeの挙動が正しくありません")

if stopwatch.get_display_time(1000) != ["00:00:01", ".00"]:
    raise Exception("get_display_timeの挙動が正しくありません")

if stopwatch.get_display_time(100000) != ["00:01:40", ".00"]:
    raise Exception("get_display_timeの挙動が正しくありません")

if stopwatch.get_display_time(10000000) != ["02:46:40", ".00"]:
    raise Exception("get_display_timeの挙動が正しくありません")

print("テストに合格しました")
