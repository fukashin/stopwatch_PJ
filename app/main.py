import customtkinter as ctk
from tkinter import font

from app.stopwatch_activity_handler import StopwatchActivityHandler

# メインウィンドウの初期化
root = ctk.CTk() 
root.title("ストップウォッチ")
root.geometry("700x400")  # 幅700px、高さ400pxのウィンドウ
root.configure(fg_color="#F0F0F0", bg_color="#F0F0F0")  # 背景色を薄いグレーに設定

# ウィンドウのサイズを固定
root.resizable(False, False)  # 幅と高さのサイズ変更を無効にする


# フォント設定
large_font = ctk.CTkFont(family="Helvetica", size=68, weight="bold")  # 大きな文字用
small_font = ctk.CTkFont(family="Helvetica", size=24, weight="bold")  # ミリ秒部分の小さな文字用
medium_font = ctk.CTkFont(family="Helvetica", size=16, weight="bold")  # 中程度の文字用

    # stopWatchactivityhandlerのインスタンス作成
activity_handler = StopwatchActivityHandler()



# メインタイム表示用フレーム
time_frame = ctk.CTkFrame(root, fg_color="#FFFFFF")  # フレームの背景色を設定
time_frame.pack(pady=10)  # 上下のマージンを調整

# メインタイム表示 (時:分:秒部分)
main_time_label = ctk.CTkLabel(time_frame, text="00: 00 : 00", font=large_font)
main_time_label.pack(side="left", anchor="s", padx=5)  # 下揃えで配置

# ミリ秒表示
millisecond_label = ctk.CTkLabel(time_frame, text=".00", font=small_font)
millisecond_label.pack(side="left", anchor="sw", pady=(20, 0))  # 下揃えで配置



# ラップタイムとスプリットタイムのラベル
label_frame = ctk.CTkFrame(root, fg_color="#F0F0F0", bg_color="#F0F0F0")  # フレームの背景色を設定
label_frame.pack(pady=10)

lap_label = ctk.CTkLabel(label_frame, text="ラップタイム", font=medium_font)
lap_label.grid(row=0, column=0, padx=45, sticky="w")

split_label = ctk.CTkLabel(label_frame, text="スプリットタイム", font=medium_font)
split_label.grid(row=0, column=1, padx=45, sticky="w")

# ラップタイムのラベルを保持するリスト
lap_time_labels = []
for i in range(3):
    lap_time = ctk.CTkLabel(label_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    lap_time.grid(row=i+1, column=0, padx=48, sticky="w")
    lap_time_labels.append(lap_time)

# スプリットタイムのラベルを保持するリスト
split_time_labels = []
for i in range(3):
    split_time = ctk.CTkLabel(label_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    split_time.grid(row=i+1, column=1, padx=48, sticky="w")
    split_time_labels.append(split_time)


# ストップウォッチを更新する関数
def update_time():
    if activity_handler.stopwatch.is_running:
        main_time_label.configure(text=activity_handler.stopwatch.display_time[0])  # ここで時間を更新
        millisecond_label.configure(text=activity_handler.stopwatch.display_time[1])  # ここで時間を更新
        # activity_handler.stopwatch.count_up()
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
        # ラップタイムとスプリットタイムを記録するメソッドを呼び出す
        activity_handler.rap_split()

        # ラップタイムを取得して表示
        rap_times = activity_handler.stopwatch.rap_display_time
 
        # ラップタイムをそのまま全てを表示
        display_times = rap_times

        # 取得したラップタイムをラベルに表示
        for i, time in enumerate(display_times):
            lap_time_labels[i].configure(text=f"{i+1}. {time}")  # ラベルを更新

        # スプリットタイムを取得して表示
        split_times = activity_handler.stopwatch.split_display_time

         # スプリットタイムをそのまま全てを表示
        display_split_times = split_times

        for i, time in enumerate(display_split_times):
            split_time_labels[i].configure(text=f"{i+1}. {time}")  # ラベルを更新


    # ストップウォッチが動作していない場合
    else:
        # ストップウォッチが動作中ならリセット処理を行う
        activity_handler.reset()

        # タイムラベルをリセット
        main_time_label.configure(text="00:00:00")
        millisecond_label.configure(text=".00")
        
        # ラップタイムとスプリットタイムのラベルをリセット
        for lap_time_label in lap_time_labels:
            lap_time_label.configure(text=f"{lap_time_labels.index(lap_time_label)+1}. -- : -- : -- : --")
        for split_time_label in split_time_labels:
            split_time_label.configure(text=f"{split_time_labels.index(split_time_label)+1}. -- : -- : -- : --")

        

# ボタンの表示を更新する関数
def update_button_label():
    if activity_handler.stopwatch.is_running:
        reset_spl_button.configure(text="スプリ/ラップ")
        start_stop_button.configure(text="ストップ")
    else:
        start_stop_button.configure(text="スタート")
        reset_spl_button.configure(text="リセット")

# ボタンの色設定
button_bg_color = "#007b99"  # ボタンの背景色
button_fg_color = "white"    # ボタンの文字色


# ボタン
button_frame = ctk.CTkFrame(root,fg_color="#F0F0F0", bg_color="#F0F0F0")
button_frame.pack(pady=20)

reset_spl_button = ctk.CTkButton(button_frame,
                                 text="リセット",
                                 font=medium_font,
                                 width=150,
                                 height=50,
                                 command=reset_spl_button,
                                 fg_color=button_bg_color,
                                 text_color=button_fg_color)
reset_spl_button.grid(row=0, column=0, padx=20)

start_stop_button = ctk.CTkButton(button_frame,
                                 text="スタート",
                                 font=medium_font,
                                 width=150,
                                 height=50,
                                 command=start_stop_stopwatch,
                                 fg_color=button_bg_color,
                                 text_color=button_fg_color)
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


