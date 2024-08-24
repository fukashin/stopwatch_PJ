import tkinter as tk
from tkinter import font

from StopWatchActivityHandler import StopWatchActivityHandler

# メインウィンドウの初期化
root = tk.Tk()
root.title("ストップウォッチ")
root.geometry("500x300")  # 幅500px、高さ300pxのウィンドウ

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

# ラップタイムの表示
for i in range(3):
    lap_time = tk.Label(label_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    lap_time.grid(row=i+1, column=0,padx=48, sticky="w")

# スプリットタイムの表示
for i in range(3):
    split_time = tk.Label(label_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    split_time.grid(row=i+1, column=1, padx=48,sticky="w")


# ストップウォッチを更新する関数
def update_time():
    if activity_handler.stopwatch.is_running:
        main_time_label.config(text=activity_handler.stopwatch.elapsed_time)  # ここで時間を更新
        root.after(10, update_time)  # 10ms後に再度この関数を呼び出す


# スタート、ストップボタンを押したときの処理関数
def start_stop_stopwatch():
    if activity_handler.stopwatch.is_running:
        activity_handler.stop()
    else:
        activity_handler.start()

# ボタンの表示を更新する関数
def update_button_label():
    if activity_handler.stopwatch.is_running:
        reset_spl_button.config(text="リセット")
        start_stop_button.config(text="スタート")
    else:
        reset_spl_button.config(text="スプリ/ラップ")
        start_stop_button.config(text="ストップ")

# ボタン
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

reset_spl_button = tk.Button(button_frame, text="リセット", font=medium_font, width=10)
reset_spl_button.grid(row=0, column=0, padx=20)

start_stop_button = tk.Button(button_frame, text="スタート", font=medium_font, width=10)
start_stop_button.grid(row=0, column=1, padx=20)

# ボタンラベルの更新
update_button_label()

# メインループ
root.mainloop()


# １ボタン押したときの処理を追加
# ２スプリとラップのボンタ処理追加
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


