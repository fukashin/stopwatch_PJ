from app.stopwatch import StopWatch

stopwatch = StopWatch()

set_display_time_0 = ["00:12:13", ".23"]
set_display_time_1 = ["00:14:15", ".46"]
set_display_time_2 = ["01:30:20", ".52"]
set_display_time_3 = ["02:10:13", ".13"]
stopwatch.set_rap_display_time(set_display_time_0)
stopwatch.set_rap_display_time(set_display_time_1)
stopwatch.set_rap_display_time(set_display_time_2)

if set_display_time_0 != stopwatch.rap_display_time[0]:
    raise Exception("record_split_timeの挙動が正しくありません")
if set_display_time_1 != stopwatch.rap_display_time[1]:
    raise Exception("record_split_timeの挙動が正しくありません")
if set_display_time_2 != stopwatch.rap_display_time[2]:
    raise Exception("record_split_timeの挙動が正しくありません")

stopwatch.set_rap_display_time(set_display_time_3)

if set_display_time_1 != stopwatch.rap_display_time[0]:
    raise Exception("record_split_timeの挙動が正しくありません")
if set_display_time_2 != stopwatch.rap_display_time[1]:
    raise Exception("record_split_timeの挙動が正しくありません")
if set_display_time_3 != stopwatch.rap_display_time[2]:
    raise Exception("record_split_timeの挙動が正しくありません")

print("テストに合格しました")
