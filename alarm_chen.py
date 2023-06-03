import tkinter as tk
from tkinter import messagebox
import time,os
import threading


class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("闹钟程序")
        self.root.geometry("300x300")
        self.root.resizable(1, 1)
        self.root.configure(bg="#f2f2f2")

        self.label = tk.Label(
            self.root,
            text="选择闹钟时间：",
            font=("Helvetica", 14),
            bg="#f2f2f2"
        )
        self.label.pack(pady=20)

        self.button_5min = tk.Button(
            self.root,
            text="5分钟",
            font=("Helvetica", 12),
            bg="#808080",
            fg="#ffffff",
            command=lambda: self.set_alarm(5)
        )
        self.button_5min.pack(pady=5)

        self.button_10min = tk.Button(
            self.root,
            text="10分钟",
            font=("Helvetica", 12),
            bg="#808080",
            fg="#ffffff",
            command=lambda: self.set_alarm(10)
        )
        self.button_10min.pack(pady=5)

        self.button_20min = tk.Button(
            self.root,
            text="20分钟",
            font=("Helvetica", 12),
            bg="#808080",
            fg="#ffffff",
            command=lambda: self.set_alarm(20)
        )
        self.button_20min.pack(pady=5)

        self.button_custom = tk.Button(
            self.root,
            text="自定义时间",
            font=("Helvetica", 12),
            bg="#808080",
            fg="#ffffff",
            command=self.show_custom_dialog
        )
        self.button_custom.pack(pady=5)

    def set_alarm(self, minutes):
        self.root.withdraw()
        threading.Timer(minutes * 60, self.trigger_alarm).start()

    def show_custom_dialog(self):
        self.root.withdraw()
        self.custom_dialog = tk.Toplevel()
        self.custom_dialog.title("自定义时间")
        self.custom_dialog.geometry("300x200")
        self.custom_dialog.resizable(False, False)
        self.custom_dialog.configure(bg="#f2f2f2")

        self.label_hour = tk.Label(
            self.custom_dialog,
            text="小时：",
            font=("Helvetica", 12),
            bg="#f2f2f2"
        )
        self.label_hour.pack(pady=5)

        self.entry_hour = tk.Entry(self.custom_dialog, font=("Helvetica", 12))
        self.entry_hour.pack(pady=5)

        self.label_minute = tk.Label(
            self.custom_dialog,
            text="分钟：",
            font=("Helvetica", 12),
            bg="#f2f2f2"
        )
        self.label_minute.pack(pady=5)

        self.entry_minute = tk.Entry(self.custom_dialog, font=("Helvetica", 12))
        self.entry_minute.pack(pady=5)

        self.button_set = tk.Button(
            self.custom_dialog,
            text="设置闹钟",
            font=("Helvetica", 12),
            bg="#808080",
            fg="#ffffff",
            command=self.set_custom_alarm
        )
        self.button_set.pack(pady=10)

    def set_custom_alarm(self):
        try:
            hour = int(self.entry_hour.get())
            minute = int(self.entry_minute.get())

            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                raise ValueError

            current_time = time.localtime()
            target_time = time.struct_time(
                (current_time.tm_year,
                current_time.tm_mon,
                current_time.tm_mday,
                 hour,
                minute,
                0,
                current_time.tm_wday,
                current_time.tm_yday,
                current_time.tm_isdst)


            )

            seconds_until_alarm = time.mktime(target_time) - time.mktime(current_time)
            self.custom_dialog.destroy()

            if seconds_until_alarm <= 0:
                messagebox.showerror("错误", "选择的时间已过，请重新设置。")
                self.root.deiconify()
            else:
                self.root.withdraw()
                threading.Timer(seconds_until_alarm, self.trigger_alarm).start()
        except ValueError:
            messagebox.showerror("错误", "请输入有效的小时和分钟。")

    def trigger_alarm(self):
        messagebox.showinfo("闹钟", "时间到！")
        os.system("convenience_store1.mp3")

        self.root.deiconify()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
