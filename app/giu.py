import tkinter as tk
from tkinter import font

# メインウィンドウの初期化
root = tk.Tk()
root.title("ストップウォッチ")
root.geometry("500x300")  # 幅500px、高さ300pxのウィンドウ

# フォント設定
large_font = font.Font(family="Helvetica", size=48, weight="bold")  # 大きな文字用
medium_font = font.Font(family="Helvetica", size=14)  # 中程度の文字用

# メインタイム表示
time_label = tk.Label(root, text="00: 00 : 00.00", font=large_font)

# ラベルを中央の上部に配置
time_label.pack(side="top", pady=20)  # 上部に配置し、上下に余白を設定

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

# ボタン
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

reset_button = tk.Button(button_frame, text="リセット", font=medium_font, width=10)
reset_button.grid(row=0, column=0, padx=20)

start_button = tk.Button(button_frame, text="スタート", font=medium_font, width=10)
start_button.grid(row=0, column=1, padx=20)

# メインループ
root.mainloop()
