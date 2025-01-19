import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class TextFileMerger:
    def __init__(self):
        # 创建主窗口
        self.window = tk.Tk()
        self.window.title("文本文件合并工具2")
        self.window.geometry("400x300")

        # 存储选中的文件路径
        self.file1_path = ""
        self.file2_path = ""

        # 创建界面元素
        self.create_widgets()

    def create_widgets(self):
        # 第一个文件选择按钮
        self.btn_file1 = tk.Button(self.window,
                                   text="选择第一个文件",
                                   command=self.select_file1)
        self.btn_file1.pack(pady=10)

        # 显示第一个文件路径的标签
        self.label_file1 = tk.Label(self.window, text="未选择文件")
        self.label_file1.pack()

        # 第二个文件选择按钮
        self.btn_file2 = tk.Button(self.window,
                                   text="选择第二个文件",
                                   command=self.select_file2)
        self.btn_file2.pack(pady=10)

        # 显示第二个文件路径的标签
        self.label_file2 = tk.Label(self.window, text="未选择文件")
        self.label_file2.pack()

        # 合并按钮
        self.btn_merge = tk.Button(self.window,
                                   text="合并文件",
                                   command=self.merge_files)
        self.btn_merge.pack(pady=20)

    def select_file1(self):
        # 打开文件选择对话框
        self.file1_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")])
        if self.file1_path:
            self.label_file1.config(text=self.file1_path)

    def select_file2(self):
        # 打开文件选择对话框
        self.file2_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")])
        if self.file2_path:
            self.label_file2.config(text=self.file2_path)

    def merge_files(self):
        # 检查是否已选择两个文件
        if not self.file1_path or not self.file2_path:
            messagebox.showerror("错误", "请先选择两个文件！")
            return

        try:
            # 读取两个文件的内容
            with open(self.file1_path, 'r', encoding='utf-8') as f1:
                content1 = f1.read()
            with open(self.file2_path, 'r', encoding='utf-8') as f2:
                content2 = f2.read()

            # 选择保存新文件的位置
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")]
            )

            if save_path:
                # 将内容写入新文件
                with open(save_path, 'w', encoding='utf-8') as f_output:
                    f_output.write(content1 + '\n' + content2)

                messagebox.showinfo("成功", "文件合并完成！")

        except Exception as e:
            messagebox.showerror("错误", f"合并文件时出错：{str(e)}")

    def run(self):
        # 运行程序
        self.window.mainloop()


if __name__ == "__main__":
    app = TextFileMerger()
    app.run()
