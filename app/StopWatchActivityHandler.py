class StopWatchActivityHandler:
    def __init__(self):
        # StopWatchクラスのインスタンスを作成し、stopwatch属性に格納
        self.stopwatch = StopWatch()

    def start(self):
        # ストップウォッチを開始
        self.stopwatch.start()

    def _start_counting(self):
        # ストップウォッチが動作中であれば
        if self.stopwatch.is_running():
            # ストップウォッチの時間を1ミリ秒進める
            self.stopwatch.count_up()
            # 次のカウントを1ミリ秒後にスケジュールする
            self._schedule_next_count()

    def _schedule_next_count(self):
        # UIフレームワークに依存するが、1ミリ秒後に再度_countingを実行するタイマーをセットする
        # 例えば、Tkinterではafterメソッドを使うことができる
        pass  # 実装が必要

    def stop(self):
        # ストップウォッチを停止
        self.stopwatch.stop()
        # カウントアップを止めるための内部メソッドを呼び出す
        self._cancel_counting()

    def _cancel_counting(self):
        # スケジュールされた次のカウントアップ呼び出しをキャンセルする
        # 実際のUIフレームワークの機能に依存する
        pass  # 実装が必要

    def rap_split(self):
        # スプリットタイムを記録する
        self.stopwatch.record_split_time()
        # ラップタイムを記録する
        self.stopwatch.record_rap_time()

    def reset(self):
        # ストップウォッチをリセットする
        self.stopwatch.reset()
