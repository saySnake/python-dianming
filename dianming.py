import tkinter
import threading
import random
import time

class bisai:

    def __init__(self):
        self.root = tkinter.Tk()
        # self.root.geometry('250x250')  # 初始化界面大小
        self.root.title('点名')
        self.root.minsize(250, 250)
        self.root.maxsize(400, 400)
        self.show()
        self.root.mainloop()

    #显示区域
    def show(self):
        self.val = tkinter.StringVar()
        self.val.set('请选择名字')

        self.zhangwei = tkinter.Label(self.root, bg='#fff', text='张')
        self.zhangwei.place(x=10, y=10, width=40, height=40)  # 像素

        self.lixin = tkinter.Label(self.root, bg='#fff', text='李')
        self.lixin.place(x=60, y=10, width=40, height=40)  # 像素

        self.yangchen = tkinter.Label(self.root, bg='#fff', text='晨', borderwidth=1)
        self.yangchen.place(x=110, y=10, width=40, height=40)  # 像素

        self.liuwenjie = tkinter.Label(self.root, bg='#fff', text='柳')
        self.liuwenjie.place(x=160, y=10, width=40, height=40)  # 像素

        self.yanghaitao = tkinter.Label(self.root, bg='#fff', text='海')
        self.yanghaitao.place(x=210, y=10, width=40, height=40)  # 像素root.mainloop()

        self.chen = tkinter.Label(self.root, bg='#fff', text='杨')
        self.chen.place(x=10, y=60, width=40, height=40)  # 像素

        self.chenkaixiang = tkinter.Label(self.root, bg='#fff', text='陈')
        self.chenkaixiang.place(x=60, y=60, width=40, height=40)  # 像素

        self.jinguo = tkinter.Label(self.root, bg='#fff', text='金')
        self.jinguo.place(x=110, y=60, width=40, height=40)  # 像素

        self.btn_start = tkinter.Button(self.root, text='开始', command=self.start,state ='normal')
        self.btn_start.place(x='70', y='100', width='50', height='50')

        self.btn_end = tkinter.Button(self.root, text='结束', command=self.stop,state ='normal')
        self.btn_end.place(x='130', y='100', width='50', height='50')

        self.label1 = tkinter.Label(self.root, textvariable=self.val, bg='pink', font=('黑体', 12), width='13')
        self.label1.place(x='60', y='150', width='150', height='50')

        # 定义一个List列表
        self.list = [self.zhangwei, self.lixin, self.yangchen, self.liuwenjie, self.yanghaitao, self.chenkaixiang, self.jinguo, self.chen]

        # 索引最大值
        self.max_index = len(self.list) - 1
        # 起使索引
        self.start_index = 0

    def start(self):
        if self.btn_start['state'] =='normal':
            self.t =threading.Thread(target=self.xunhuan)
            self.btn_start['state']='disabled'
            self.btn_end['state']='normal'
            self.t.start()


        self.btn_start['state'] ='disabled'

    def stop(self):
        self.btn_start['state'] ='normal'
        self.btn_end['state']='disabled'


    def xunhuan(self):
        while True:
            if self.btn_start['state'] =='normal':
                self.btn_start['state']='normal'
                self.btn_end['state']='disabled'
                return
            time.sleep(0.05)

            for self.i in self.list:
                self.i['bg']='blue'

            #当前选择的颜色为红色
            self.list[self.start_index]['bg'] ='red'
            #拼接
            self.val.set(self.list[self.start_index]['text'])
            #索引加1
            self.start_index=random.randrange(0,7)
            self.start_index +=1
            if self.start_index >self.max_index:
                self.start_index =0


kaishi =bisai()