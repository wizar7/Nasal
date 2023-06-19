import tkinter as tk
from threading import Thread
from queue import Queue

def read_data(queue):
    # 模拟实时获取数据的函数
    # 这里使用随机数生成一个示例数据
    import random
    while True:
        data = random.randint(1, 100)
        queue.put(data)

def display_data(queue):
    def update_label():
        # 更新标签的函数
        if not queue.empty():
            data = queue.get()
            data_label.config(text="Data: {}".format(data))
        data_label.after(100, update_label)

    # 创建GUI窗口
    window = tk.Tk()
    window.title("Real-time Data Display")

    # 创建标签
    data_label = tk.Label(window, text="Data: ")
    data_label.pack()

    # 更新标签
    update_label()

    # 运行GUI主循环
    window.mainloop()

if __name__ == '__main__':
    # 创建线程间通信的队列
    queue = Queue()

    # 创建读取数据的线程
    read_thread = Thread(target=read_data, args=(queue,))
    read_thread.start()

    # 创建显示数据的GUI程序
    display_data(queue)

    # 等待读取数据的线程结束
    read_thread.join()
