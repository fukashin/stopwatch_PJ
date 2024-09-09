import datetime
import time


class StopWatch:

    # コンストラクター
    def __init__(self):
        # 属性定義と初期化
        self.elapsed_time: int = 0
        self.is_running: bool = False
        self.rap_time: list = []
        self.split_time: list = []
        self.display_time = self.get_display_time(0) # [ ["XX:XX:XX", ".XX"], ... ]
        self.rap_display_time: list = [] # ["XX:XX:XX.XX", ...]
        self.split_display_time: list = [] # ["XX:XX:XX.XX", ...]

    # メソッド
    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False
        self.count_up_time = None

    def record_split_time(self):
        self.split_time.append(self.elapsed_time)
        # スプリットタイムをフォーマットされた形式で格納
        split_display_time: list = self.get_display_time(self.split_time[-1])
        # XX:XX:XX.XX の形式で格納
        self.set_split_display_time(split_display_time[0] + split_display_time[1])

    def record_rap_time(self):
        if self.split_time.__len__() == 1:
            # スプリットタイムが1つの時はそのままラップタイムとして格納
            self.rap_time.append(self.split_time[0])
        elif self.split_time.__len__() >= 2:
            # 直近2つのスプリットタイムの差分を格納
            rap_time = self.split_time[-1] - self.split_time[-2]
            self.rap_time.append(rap_time)
        else:
            raise Exception("ラップタイム取得中にエラーが発生しました")
        # ラップタイムをフォーマットされた形式で格納
        rap_display_time: list = self.get_display_time(self.rap_time[-1])
        # XX:XX:XX.XX の形式で格納
        self.set_rap_display_time(rap_display_time[0] + rap_display_time[1])
        
    def reset(self):
        if not self.is_running:
            # 停止中は全ての値を初期状態に戻す
            self.elapsed_time = 0
            self.rap_time.clear()
            self.split_time.clear()
            self.display_time = self.get_display_time(0)
            self.rap_display_time.clear()
            self.split_display_time.clear()
            self.count_up_time: datetime = None
        else:
            raise Exception("動作中にリセットが実行されました")
        
    def count_up(self):
        while self.is_running:
            if self.elapsed_time < 359999999:
                time.sleep(1/1000) # 1ミリ秒ごとにカウントアップ
                self.elapsed_time += 1

    def get_display_time(self, milliseconds):
        # timedelta型に変換
        timedelta = datetime.timedelta(milliseconds=milliseconds)
        # 時:分:秒.ミリ秒の計算
        total_seconds = int(timedelta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = timedelta.microseconds // 10000  # ミリ秒を2桁に丸める
        # 時:分:秒と.ミリ秒に分けて配列として戻す
        return [f"{hours:02}:{minutes:02}:{seconds:02}", f".{milliseconds:02}"]        

    def set_split_display_time(self, split_display_time):
        if self.split_display_time.__len__() == 3:
            # 要素数が3つの時は一番古いデータを削除する
            self.split_display_time.pop(0)
        self.split_display_time.append(split_display_time)

    def set_rap_display_time(self, rap_display_time):
        if self.rap_display_time.__len__() == 3:
            # 要素数が3つの時は一番古いデータを削除する
            self.rap_display_time.pop(0)
        self.rap_display_time.append(rap_display_time)

