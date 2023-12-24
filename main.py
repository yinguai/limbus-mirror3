import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class AutoClickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("边狱巴士坐牢小助手")

        style = ttk.Style()
        style.configure("Red.TButton", foreground="black", background="red", padding=(10, 5))
        style.configure("Yellow.TButton", foreground="black", background="yellow", padding=(10, 5))
        style.configure("Blue.TButton", foreground="black", background="blue", padding=(10, 5))

        self.btn_mirror_enter = ttk.Button(master, text="主界面点击", style="Red.TButton", command=self.run_mirror_enter)
        self.btn_mirror_enter.pack(pady=10)

        self.btn_battle = ttk.Button(master, text="战斗", style="Yellow.TButton", command=self.run_battle_scripts)
        self.btn_battle.pack(pady=10)

        self.btn_reward = ttk.Button(master, text="奖励领取", style="Blue.TButton", command=self.run_reward)
        self.btn_reward.pack(pady=10)

    def run_mirror_enter(self):
        try:
            subprocess.run(['python', 'mirror_enter.py'])
        except Exception as e:
            messagebox.showerror("错误", f"发生错误：{str(e)}")

    def run_battle_scripts(self):
        battle_scripts = ['.\\battle_boss.py', '.\\battle_what.py', '.\\battle_hard.py','.\\battle_normal.py','.\\battle_shop.py']
        for script in battle_scripts:
            try:
                subprocess.run(['python', script])
            except Exception as e:
                messagebox.showerror("错误", f"发生错误：{str(e)}")
        messagebox.showinfo("完成", "所有战斗脚本已执行完毕")

    def run_reward(self):
        try:
            subprocess.run(['python', 'reward.py'])
        except Exception as e:
            messagebox.showerror("错误", f"发生错误：{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerGUI(root)
    root.geometry("300x200")  # 设置窗口大小
    root.mainloop()
