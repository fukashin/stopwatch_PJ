import time


class StopWatch:
    def __init__(self):
        # コンストラクターの中で初期化処理を行う
        self.elapsed_time: int = 0
        self.is_running: bool = False
        self.rap_time: list = []
        self.split_time: list = []
