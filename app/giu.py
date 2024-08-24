import tkinter as tk
from tkinter import font

from StopWatchActivityHandler import StopWatchActivityHandler

# メインウィンドウの初期化
root = tk.Tk()
root.title("ストップウォッチ")
root.geometry("700x400")  # 幅500px、高さ300pxのウィンドウ

# フォント設定
large_font = font.Font(family="Helvetica", size=48, weight="bold")  # 大きな文字用
small_font = font.Font(family="Helvetica", size=24, weight="bold")  # ミリ秒部分の小さな文字用
medium_font = font.Font(family="Helvetica", size=14)  # 中程度の文字用

    # StopWatchActivityHandlerのインスタンス作成
activity_handler = StopWatchActivityHandler()



# メインタイム表示用フレーム
time_frame = tk.Frame(root)
time_frame.pack(pady=20)

# メインタイム表示 (時:分:秒部分)
main_time_label = tk.Label(time_frame, text="00: 00 : 00", font=large_font)
main_time_label.pack(side="left", anchor="s")  # 下揃えで配置

# ミリ秒表示
millisecond_label = tk.Label(time_frame, text=".00", font=small_font)
millisecond_label.pack(side="left", anchor="sw", pady=(30, 0))  # 下揃えで配置



# ラップタイムとスプリットタイムのラベル
label_frame = tk.Frame(root)
label_frame.pack(pady=10)


lap_label = tk.Label(label_frame, text="ラップタイム", font=medium_font)
lap_label.grid(row=0, column=0, padx=45, sticky="w")

split_label = tk.Label(label_frame, text="スプリットタイム", font=medium_font)
split_label.grid(row=0, column=1, padx=45, sticky="w")

# ラップタイムのラベルを保持するリスト
lap_time_labels = []
for i in range(3):
    lap_time = tk.Label(label_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    lap_time.grid(row=i+1, column=0, padx=48, sticky="w")
    lap_time_labels.append(lap_time)

# スプリットタイムのラベルを保持するリスト
split_time_labels = []
for i in range(3):
    split_time = tk.Label(label_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    split_time.grid(row=i+1, column=1, padx=48, sticky="w")
    split_time_labels.append(split_time)


# ストップウォッチを更新する関数
def update_time():
    if activity_handler.stopwatch.is_running:
        main_time_label.config(text=activity_handler.stopwatch.elapsed_time)  # ここで時間を更新
        activity_handler.stopwatch.count_up()
        root.after(10, update_time)  # 10ms後に再度この関数を呼び出す


# スタート、ストップボタンを押したときの処理関数
def start_stop_stopwatch():
    if activity_handler.stopwatch.is_running:
        activity_handler.stop()
        update_button_label()
    else:
        activity_handler.start()
        update_button_label()
        update_time()

# リセット、スプリ/ラップボタンを押したときの処理関数
def reset_spl_button():
    # ストップウォッチが動作中かどうかを確認
    if activity_handler.stopwatch.is_running:

        test_time = activity_handler.stopwatch.elapsed_time
        print(test_time)

        # ラップタイムとスプリットタイムを記録するメソッドを呼び出す
        activity_handler.rap_split()

        # ラップタイムを取得して表示
        rap_times = activity_handler.stopwatch.rap_time
        # ラップタイムの要素数が表示以上か判定
        if len(rap_times) >= len(lap_time_labels):
            # ラップタイムが3つ以上ある場合、後ろから3つの要素を取り出す
            display_times = rap_times[-len(lap_time_labels):]  # 後ろから3つの要素を取得
        else:
            # ラップタイムが3つ未満の場合、そのまま全てを表示
            display_times = rap_times

        # 取得したラップタイムをラベルに表示
        for i, time in enumerate(display_times):
            lap_time_labels[i].config(text=f"{i+1}. {time}")  # ラベルを更新

        # スプリットタイムを取得して表示
        split_times = activity_handler.stopwatch.split_time
        if len(split_times) >= len(split_time_labels):
            # スプリットタイムも後ろから3つの要素を取り出す
            display_split_times = split_times[-len(split_time_labels):]
        else:
            # スプリットタイムが3つ未満の場合、そのまま全てを表示
            display_split_times = split_times

        for i, time in enumerate(display_split_times):
            split_time_labels[i].config(text=f"{i+1}. {time}")  # ラベルを更新


    # ストップウォッチが動作していない場合
    else:
        # ストップウォッチが動作中ならリセット処理を行う
        activity_handler.reset()

        # リセット後のラップタイムを取得して表示
        rap_times = activity_handler.stopwatch.rap_time
        # 取得したラップタイムをラベルに表示（最大で3つのラップタイムまで）
        for i, time in enumerate(rap_times):
            if i < len(lap_time_labels):  # ラベルの数に応じて表示を制限
                lap_time_labels[i].config(text=f"{i+1}. {time}")  # ラベルを更新

        # リセット後のスプリットタイムを取得して表示
        split_times = activity_handler.stopwatch.split_time
        # 取得したスプリットタイムをラベルに表示（最大で3つのスプリットタイムまで）
        for i, time in enumerate(split_times):
            if i < len(split_time_labels):  # ラベルの数に応じて表示を制限
                split_time_labels[i].config(text=f"{i+1}. {time}")  # ラベルを更新
        

# ボタンの表示を更新する関数
def update_button_label():
    if activity_handler.stopwatch.is_running:
        reset_spl_button.config(text="スプリ/ラップ")
        start_stop_button.config(text="ストップ")
    else:
        start_stop_button.config(text="スタート")
        reset_spl_button.config(text="リセット")



# ボタン
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

reset_spl_button = tk.Button(button_frame, text="リセット", font=medium_font, width=10,command=reset_spl_button)
reset_spl_button.grid(row=0, column=0, padx=20)

start_stop_button = tk.Button(button_frame, text="スタート", font=medium_font, width=10,command=start_stop_stopwatch)
start_stop_button.grid(row=0, column=1, padx=20)

# 初期のボタンラベルの更新
update_button_label()

# メインループ
root.mainloop()


# １ボタン押したときの処理を追加
# ２スプリとラップのボタン処理追加
# ３スプリラップ表示
# ４時間の更新
# ５時間の表示


# # ボタンの作成と関数の関連付け
# button_frame = tk.Frame(root)
# button_frame.pack(pady=20)

# reset_button = tk.Button(button_frame, text="リセット", font=medium_font, width=10, command=reset_stopwatch)
# reset_button.grid(row=0, column=0, padx=20)

# start_stop_button = tk.Button(button_frame, text="スタート", font=medium_font, width=10, command=start_stop_stopwatch)
# start_stop_button.grid(row=0, column=1, padx=20)


