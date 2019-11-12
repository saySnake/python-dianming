#布局
#添加文件
    #弹出选择文件的对话框
    #将文件信息显示在显示面板

#压缩
    #弹出对话框选择压缩路径
    #获取显示面板信息对文件进行压缩
    #压缩成功弹出提示框

#解压
    #用户选择解压文件
    #选择解压路径
    #解压成功弹出提示框
import tkinter
import tkinter.filedialog
import zipfile
import os
import tkinter.messagebox

class yasuo:
     def __init__(self):
         self.root = tkinter.Tk()
         self.root.minsize(300, 300)
         self.root.title('压缩器')
         self.showText()
         self.root.mainloop()


     def showText(self):
         self.btn_add = tkinter.Button(self.root, text='添加文件', command=self.press_add).grid(row=0, column=0)
         btn_ys = tkinter.Button(self.root, text='压缩文件', command=self.press_ys).grid(row=0, column=1)
         btn_jy = tkinter.Button(self.root, text='解压文件', command=self.press_jy).grid(row=0, column=2)
         self.val = tkinter.StringVar()
         self.val.set('')
         label = tkinter.Label(self.root, textvariable=self.val, bg='pink', width=50).grid(row=1, column=0, columnspan=3)

        #添加文件
     def press_add(self):
         self.paths =tkinter.filedialog.askopenfilenames()
         # 将文件路径转换为字符窜并换行输出
         self.strfile ='\n'.join(self.paths)
         if self.val.get() =='':
             # 将文件信息写入显示面板
            self.val.set(self.strfile)
            tkinter.messagebox.showinfo('提示','添加文件成功')

     def press_ys(self):
         #判断如果没有压缩路径给提示
         print(self.val.get())

         if self.val.get() !='':
             #弹出对话框返回压缩路径
             self.dirpath =tkinter.filedialog.askdirectory(title='请选择压缩路径')
             print(self.dirpath)
             self.zf =zipfile.ZipFile(self.dirpath+'/压缩.zip','w')
             #遍历文件
             for i in self.paths:
                 self.zf.write(i,os.path.basename(i))
                 self.zf.close()
                 #压缩成功给提示
                 tkinter.messagebox.showinfo('压缩成功提示','压缩成功,压缩路径：'+self.dirpath+'/压缩.zip')
         else:
             tkinter.messagebox.showinfo('提示','请添加文件')

         #解压
     def press_jy(self):
         #判断添加的文件是不是为空
         if self.val.get() !='':
             #选择压缩文件
             self.jypath =tkinter.filedialog.askopenfilename(title ='选择解压路径',filetypes =[('zip file','*.zip')])
             #压缩路径
             self.zippath =tkinter.filedialog.askdirectory(title='选择解压路径')
             #解压
             self.zf =zipfile.ZipFile(self.jypath,'r')
             self.zf.extractall(self.zippath)
             #弹出提示框
             tkinter.messagebox.showinfo('提示','解压成功，解压路径：'+self.zippath)
         else:
             tkinter.messagebox.showinfo('提示','添加的解压文件路径为空')

kasihi =yasuo()
