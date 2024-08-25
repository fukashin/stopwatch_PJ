from app.stopwatch import StopWatch

stopwatch = StopWatch()


def check_parameter():
    check_elapsed_time = stopwatch.elapsed_time == 0
    check_is_running = stopwatch.is_running == False
    check_rap_time = stopwatch.rap_time == []
    check_split_time = stopwatch.split_time == []
    check_display_time = stopwatch.display_time == "00:00:00.00"
    return check_elapsed_time & check_is_running & check_rap_time & check_split_time & check_display_time

stopwatch.elapsed_time = 1231
stopwatch.is_running = False
stopwatch.rap_time: list = []
stopwatch.split_time: list = []
stopwatch.display_time = "00:00:21:11"
stopwatch.reset()

if not check_parameter():
    raise Exception("resetの挙動が正しくありません")

check_exception: bool

stopwatch.elapsed_time = 1231
stopwatch.is_running = True
stopwatch.rap_time: list = []
stopwatch.split_time: list = []
stopwatch.display_time = "00:00:21:11"

try:
    stopwatch.reset()
    check_exception = True
except:
    check_exception = False

if check_exception:
    raise Exception("resetの挙動が正しくありません")

print("テストに合格しました")
