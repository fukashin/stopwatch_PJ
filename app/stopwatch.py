import time


class StopWatch:

    # コンストラクター
    def __init__(self):
        self.elapsed_time: int = 0
        self.is_running: bool = False
        self.rap_time: list = []
        self.split_time: list = []

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
        else:
            raise Exception("動作中にリセットが実行されました")