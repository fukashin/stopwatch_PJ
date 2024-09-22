from app.stopwatch import StopWatch

stopwatch = StopWatch()


def check_parameter():
    check_elapsed_time = stopwatch.elapsed_time == 0
    check_is_running = stopwatch.is_running == False
    check_rap_time = stopwatch.rap_time == []
    check_split_time = stopwatch.split_time == []
    check_display_time = stopwatch.display_time == ["00:00:00", ".00"]
    check_rap_display_time = stopwatch.rap_display_time == []
    check_sprit_display_time = stopwatch.split_display_time == []
    return check_elapsed_time & check_is_running & check_rap_time & check_split_time & check_display_time & check_rap_display_time & check_sprit_display_time


# is_runningがFalseの時のテスト
stopwatch.elapsed_time = 1231
stopwatch.is_running = False
stopwatch.rap_time: list = [1231]
stopwatch.split_time: list = [1231]
stopwatch.display_time = ["00:00:21", ".14"]
stopwatch.rap_display_time: list = ["00:00:21.14"]
stopwatch.split_display_time: list = ["00:00:21.14"]
stopwatch.reset()

if not check_parameter():
    raise Exception("resetの挙動が正しくありません")

# is_runningがTrueの時のテスト
check_exception: bool

stopwatch.elapsed_time = 1231
stopwatch.is_running = True
stopwatch.rap_time: list = ["00:00:21:11"]
stopwatch.split_time: list = ["00:00:21:11"]
stopwatch.display_time = "00:00:21:11"
stopwatch.rap_display_time: list = ["00:00:21:11.14"]
stopwatch.split_display_time: list = ["00:00:21:11.14"]

try:
    stopwatch.reset()
    check_exception = True
except:
    check_exception = False

if check_exception:
    raise Exception("resetの挙動が正しくありません")

print("テストに合格しました")
