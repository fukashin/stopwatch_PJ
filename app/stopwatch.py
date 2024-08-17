import time


class StopWatch:

    # コンストラクター
    def __init__(self):
        self.elapsed_time: int = 0
        self.is_running: bool = False
        self.rap_time: list = []
        self.split_time: list = []

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def record_split_time(self):
        self.split_time.append(self.elapsed_time)