import os
import glob
import glob
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("视频色彩还原")
        self.root.geometry('600x140')  # 设置窗口大小
        self.directory = tk.StringVar()
        self.progress = tk.DoubleVar()
        self.progress_text = tk.StringVar()

        frame = tk.Frame(root)
        frame.pack(expand=True, fill='both')

        tk.Label(frame, text="选择路径:").grid(row=0, column=0, sticky='w')
        tk.Entry(frame, textvariable=self.directory).grid(row=0, column=1, sticky='we')
        tk.Button(frame, text="浏览", command=self.browse).grid(row=0, column=2, sticky='e')

        tk.Button(frame, text="开始转换", command=self.start_convert).grid(row=1, column=0, columnspan=3)

        self.status = tk.StringVar()
        tk.Label(frame, textvariable=self.status, width=100, anchor='w').grid(row=2, column=0, columnspan=4)  # 限制状态标签的宽度
        self.progress_bar = ttk.Progressbar(frame, length=200, mode='determinate', variable=self.progress)
        self.progress_bar.grid(row=3, column=0, columnspan=3, sticky='we')
        tk.Label(frame, textvariable=self.progress_text, background=self.root.cget('bg')).grid(row=4, column=1)  # 在进度条下方显示几分之几的文本

    def browse(self):
        self.directory.set(filedialog.askdirectory())

    def start_convert(self):
        directory = self.directory.get()
        files = glob.glob(os.path.join(directory, '*.mp4'))
        total = len(files)
        self.progress.set(0)  # 设置初始进度
        self.progress_text.set(f'0/{total} (0.00%)')  # 设置初始进度文本
        threading.Thread(target=self.convert, args=(total,)).start()  # 将total作为参数传递给convert方法

    def convert(self, total):
        directory = self.directory.get()
        new_directory = os.path.join(directory, '色彩还原')
        os.makedirs(new_directory, exist_ok=True)

        files = glob.glob(os.path.join(directory, '*.mp4'))

        for i, filename in enumerate(files, start=1):
            new_filename = os.path.join(new_directory, os.path.basename(filename))
            if os.path.exists(new_filename):  # 如果文件已经存在，跳过这个文件
                self.progress.set((i/total) * 100)
                self.progress_text.set(f'{i}/{total} ({self.progress.get():.2f}%)')  # 更新进度条上的文本
                self.root.update()
                continue
            command = f'ffmpeg -i {filename} -vf "lut3d=DJI.cube" -map_metadata 0 -vsync 1 {new_filename}'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            line = ''
            while True:
                char = process.stdout.read(1).decode(errors='ignore')
                if char == '' and process.poll() is not None:
                    break
                line += char
                if char == '\n':
                    self.status.set(line.strip())
                    self.root.update()
                    line = ''
                elif char == '\r':
                    self.status.set(line.strip())
                    self.root.update()
                    line = ''
            while True:
                output = process.stdout.readline().decode()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.status.set(output.strip())
                    self.root.update()

            self.progress.set((i/total) * 100)
            self.progress_text.set(f'{i}/{total} ({self.progress.get():.2f}%)')  # 更新进度条上的文本
            self.root.update()



root = tk.Tk()
app = App(root)
root.mainloop()
