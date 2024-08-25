import datetime


class StopWatch:

    # コンストラクター
    def __init__(self):
        self.elapsed_time: int = 0
        self.is_running: bool = False
        self.rap_time: list = []
        self.split_time: list = []
        self.display_time = self.get_display_time()

    # メソッド
    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def record_split_time(self):
        self.split_time.append(self.elapsed_time)

    def record_rap_time(self):
        if self.split_time.__len__() == 1:
            self.rap_time.append(self.split_time[0])
        elif self.split_time.__len__() >= 2:
            rap_time = self.split_time[-1] - self.split_time[-2]
            self.rap_time.append(rap_time)
        else:
            raise Exception("ラップタイム取得中にエラーが発生しました")
        
    def reset(self):
        if not self.is_running:
            self.elapsed_time = 0
            self.rap_time.clear()
            self.split_time.clear()
            self.display_time = self.get_display_time()
        else:
            raise Exception("動作中にリセットが実行されました")
        
    def count_up(self):
        self.elapsed_time += 1
        self.display_time = self.get_display_time()

    def get_display_time(self):
        timedelta = datetime.timedelta(milliseconds=self.elapsed_time)
        total_seconds = int(timedelta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = timedelta.microseconds // 10000  # ミリ秒を2桁に丸める
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
