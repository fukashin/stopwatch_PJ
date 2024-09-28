from app.stopwatch import StopWatch

stopwatch = StopWatch()

if stopwatch.elapsed_time != 0:
    raise Exception("elapsed_timeが正しく初期化されていません")

if stopwatch.is_running:
    raise Exception("is_runningが正しく初期化されていません")

if stopwatch.rap_time != []:
    raise Exception("rap_timeが正しく初期化されていません")

if stopwatch.split_time != []:
    raise Exception("split_timeが正しく初期化されていません")

if stopwatch.display_time != ["00:00:00", ".00"]:
    raise Exception("display_timeが正しく初期化されていません")

if stopwatch.rap_display_time != []:
    raise Exception("rap_display_timeが正しく初期化されていません")

if stopwatch.split_display_time != []:
    raise Exception("split_display_timeが正しく初期化されていません")

print("テストに合格しました")
