import unittest
from unittest.mock import MagicMock
from app.stopwatch_activity_handler import StopwatchActivityHandler

# StopwatchActivityHandler のテストクラスを作成
class TestStopwatchActivityHandler(unittest.TestCase):
    def setUp(self):
        # 各テストの前に呼ばれるセットアップメソッド
        # StopwatchActivityHandler のインスタンスを作成
        self.handler = StopwatchActivityHandler()
        
        # stopwatch の各メソッドをモック化
        # つまり、テスト用にメソッドの動作を置き換える
        self.handler.stopwatch.start = MagicMock()
        self.handler.stopwatch.stop = MagicMock()
        self.handler.stopwatch.count_up = MagicMock()
        self.handler.stopwatch.record_split_time = MagicMock()
        self.handler.stopwatch.record_rap_time = MagicMock()
        self.handler.stopwatch.reset = MagicMock()

    def test_start(self):
        # start メソッドのテスト
        self.handler.start()
        self.handler.stopwatch.start.assert_called_once()
        self.handler.stopwatch.count_up.assert_called_once()
        print("test_start: StopwatchActivityHandler の start メソッドが正しく動作しました。")

    def test_stop(self):
        # stop メソッドのテスト
        self.handler.stop()
        self.handler.stopwatch.stop.assert_called_once()
        print("test_stop: StopwatchActivityHandler の stop メソッドが正しく動作しました。")

    def test_rap_split(self):
        # rap_split メソッドのテスト
        self.handler.rap_split()
        self.handler.stopwatch.record_split_time.assert_called_once()
        self.handler.stopwatch.record_rap_time.assert_called_once()
        print("test_rap_split: StopwatchActivityHandler の rap_split メソッドが正しく動作しました。")

    def test_reset(self):
        # reset メソッドのテスト
        self.handler.reset()
        self.handler.stopwatch.reset.assert_called_once()
        print("test_reset: StopwatchActivityHandler の reset メソッドが正しく動作しました。")

if __name__ == '__main__':
    # テストの実行とカスタムメッセージの出力
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStopwatchActivityHandler)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    