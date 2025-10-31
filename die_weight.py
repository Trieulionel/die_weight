import tkinter as tk
from tkinter import messagebox

def calc_weight():
    try:
        w_g = float(entry.get())
        if w_g < 0:
            raise ValueError("負の値は入力できません。")

        # グラム → キログラムに変換
        w = w_g / 1000

        if w < 0.05:
            result.set("―（表示なし）")
        elif w < 1:
            display = round(w * 10) / 10  # 0.1kg単位
            result.set(f"{display:.1f} kg")
        elif w < 25:
            display = round(w * 2) / 2  # 0.5kg単位
            result.set(f"{display:.1f} kg")
        else:
            display = round(w)  # 1kg単位
            result.set(f"{display:.0f} kg")

    except ValueError:
        messagebox.showerror("エラー", "有効な数値（グラム）を入力してください。")

# ウィンドウ設定
root = tk.Tk()
root.title("単品金型重量 表示計算ツール（グラム入力）")
root.geometry("420x230")
root.resizable(False, False)

# ラベルと入力欄
tk.Label(root, text="実際の金型重量を入力してください（g）:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=15, justify="center")
entry.pack()

# ボタン
tk.Button(root, text="計算する", font=("Arial", 12), command=calc_weight).pack(pady=10)

# 結果表示
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

# 実行
root.mainloop()
