import tkinter as tk
from tkinter import font

# メインウィンドウの初期化
root = tk.Tk()
root.title("ストップウォッチ")
root.geometry("500x300")

# フォント設定
large_font = font.Font(family="Helvetica", size=48, weight="bold")
medium_font = font.Font(family="Helvetica", size=14)

# メインタイム表示
time_frame = tk.Frame(root)
time_frame.pack(pady=20)

lap_time_label = tk.Label(time_frame, text="00: 00 : 00", font=large_font)
lap_time_label.grid(row=0, column=0, padx=10)

split_time_label = tk.Label(time_frame, text="00: 00 : 00.00", font=large_font)
split_time_label.grid(row=0, column=1, padx=10)

# ラップタイムとスプリットタイムのラベル
lap_label = tk.Label(time_frame, text="ラップタイム", font=medium_font)
lap_label.grid(row=1, column=0)

split_label = tk.Label(time_frame, text="スプリットタイム", font=medium_font)
split_label.grid(row=1, column=1)

# ラップタイムとスプリットタイムの表示
times_frame = tk.Frame(root)
times_frame.pack()

# ラップタイムの表示
for i in range(3):
    lap_time = tk.Label(times_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    lap_time.grid(row=i, column=0, padx=5)

# スプリットタイムの表示
for i in range(3):
    split_time = tk.Label(times_frame, text=f"{i+1}. -- : -- : --", font=medium_font)
    split_time.grid(row=i, column=1, padx=5)

# ボタン
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

reset_button = tk.Button(button_frame, text="リセット", font=medium_font, width=10)
reset_button.grid(row=0, column=0, padx=20)

start_button = tk.Button(button_frame, text="スタート", font=medium_font, width=10)
start_button.grid(row=0, column=1, padx=20)

# メインループ
root.mainloop()
