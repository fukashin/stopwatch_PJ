# StopWatchActivityHandler.py
# from 呼び出し元ファイル名　import 呼び出しクラス　で参照できるようになる
from stopwatch import StopWatch
import threading

class StopwatchActivityHandler:
    def __init__(self):
        # StopWatchクラスのインスタンスを作成し、stopwatch属性に格納
        self.stopwatch = StopWatch()

    def start(self):
        # ストップウォッチを開始
        self.stopwatch.start()
        threading.Thread(target=self.stopwatch.count_up).start()

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
