class StopWatchActivityHandler:
    def __init__(self):
        # StopWatchクラスのインスタンスを作成し、stopwatch属性に格納
        self.stopwatch = StopWatch()

    def start(self):
        # ストップウォッチを開始
        self.stopwatch.start()

    def stop(self):
        # ストップウォッチを停止
        self.stopwatch.stop()

    def rap_split(self):
        # スプリットタイムを記録する
        self.stopwatch.record_split_time()
        # ラップタイムを記録する
        self.stopwatch.record_rap_time()

    def reset(self):
        # ストップウォッチをリセットする
        self.stopwatch.reset()
