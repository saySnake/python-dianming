import tkinter


class Calc:
    #初始化界面
    def __init__(self):
        # 运算表达式列表
        self.yslists = []

        # 运算标志（是否按下了运算按钮 True按了  False没按）
        self.isys = False

        self.isequal = False
        
        #放后面
        self.rootWindows()

    #初始化共用属性


    def rootWindows(self):
        root = tkinter.Tk()
        root.title('计算器')
        root.minsize(300, 300)
        # 创建变量
        self.num = tkinter.StringVar()
        self.num.set(0)
        # 创建Label显示运算结果
        label = tkinter.Label(root, textvariable=self.num, bg='gray', font=('黑体', 20), anchor='e')
        label.place(x=10, y=10, width=250, height=30)
        # 按钮
        button0 = tkinter.Button(root, text='0', command=lambda: self.pressno('0'))
        button0.place(x=10, y=250, width=100, height=50)

        button1 = tkinter.Button(root, text='1', command=lambda: self.pressno('1'))
        button1.place(x=10, y=50, width=50, height=50)

        button2 = tkinter.Button(root, text='2', command=lambda: self.pressno('2'))
        button2.place(x=60, y=50, width=50, height=50)

        button3 = tkinter.Button(root, text='3', command=lambda: self.pressno('3'))
        button3.place(x=110, y=50, width=50, height=50)

        button4 = tkinter.Button(root, text='4', command=lambda: self.pressno('4'))
        button4.place(x=10, y=100, width=50, height=50)

        button5 = tkinter.Button(root, text='5', command=lambda: self.pressno('5'))
        button5.place(x=60, y=100, width=50, height=50)

        button6 = tkinter.Button(root, text='6', command=lambda: self.pressno('6'))
        button6.place(x=110, y=100, width=50, height=50)

        button7 = tkinter.Button(root, text='7', command=lambda: self.pressno('7'))
        button7.place(x=10, y=150, width=50, height=50)

        button8 = tkinter.Button(root, text='8', command=lambda: self.pressno('8'))
        button8.place(x=60, y=150, width=50, height=50)

        button9 = tkinter.Button(root, text='9', command=lambda: self.pressno('9'))
        button9.place(x=110, y=150, width=50, height=50)

        buttonC = tkinter.Button(root, text='C', command=self.clear)
        buttonC.place(x=10, y=200, width=50, height=50)
        dian = tkinter.Button(root, text='.', command=lambda: self.pressys('.'))
        dian.place(x=60, y=200, width=50, height=50)
        yu = tkinter.Button(root, text='%', command=lambda: self.pressys('%'))
        yu.place(x=110, y=200, width=50, height=50)
        ad = tkinter.Button(root, text='+', command=lambda: self.pressys('+'))
        ad.place(x=160, y=50, width=50, height=50)
        jian = tkinter.Button(root, text='-', command=lambda: self.pressys('-'))
        jian.place(x=160, y=100, width=50, height=50)
        chengyi = tkinter.Button(root, text='*', command=lambda: self.pressys('*'))
        chengyi.place(x=160, y=150, width=50, height=50)
        chuyi = tkinter.Button(root, text='/', command=lambda: self.pressys('/'))
        chuyi.place(x=160, y=200, width=50, height=50)
        dengyu = tkinter.Button(root, text='=', command=self.getresult)
        dengyu.place(x=110, y=250, width=100, height=50)
        root.mainloop()

    # 按钮操作
    def pressno(self,no):
        global isys
        # 判断用户是否按下了运算按钮
        if self.isequal == True:
            self.num.set(0)

        if self.isys == True:
            # 按下了运算按钮
            self.num.set(no)
            # 将运算标志复位
            isys = False

        else:
            # 没有按下
            # 判断界面原是数字是否为0
            oldNo = self.num.get()
            if oldNo == '0':
                # 如果界面为0 ，获取用户按下的数字，显示到界面中
                self.num.set(no)
            else:
                # 如果界面不为0，其他数字链接起来
                self.num.set(self.num.get() + no)

    # 定义运算按钮操作
    def pressys(self,flag):
        # 全局变量
        global isys
        global yslists

        # 设置运算被按下的标志
        self.isys = True

        # 将每次运算操作的信息计入一个列表eval函数就是实现list、dict、tuple与str之间的转化
        # 按下按钮获取界面中已经输入的数字
        self.yslists.append(self.num.get())
        # 记录当前运算符号
        self.yslists.append(flag)
        print(self.yslists)

    # 获取运算结果
    def getresult(self):
        # 进行运算操作
        self.isequal = True
        # 获取当前界面的数字，并且加入运算列表
        self.yslists.append(self.num.get())
        print(self.yslists)

        # 进行运算操作
        result = eval(''.join(self.yslists))
        print(result)

        # 将结果放入界面
        self.num.set(result)
        self.yslists = []

    def clear(self):
        self.num.set(0)

c =Calc()