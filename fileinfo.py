#17377156  朱奂璋
#GUI界面设计

from tkinter import *                                 #从tkinter库中导入*
class Reg (Frame):                                    #使用Frame方法（首先定义Reg类）
    def __init__(self,master):                        #定义__init__方法
        frame = Frame(master)                         #指定Frame中的父窗口为frame
        frame.pack()                                  #使用pack类
        self.lab1 = Label(frame,text = "用户名")      
        self.lab1.grid(row = 0,column = 0,sticky = W)  
        self.ent1 = Entry(frame)  
        self.ent1.grid(row = 0,column = 1,sticky = W)  
        self.lab2 = Label(frame,text = "密码")  
        self.lab2.grid(row = 1,column = 0)  
        self.ent2 = Entry(frame,show = "*")          #使输入的密码显示为“*”
        self.ent2.grid(row = 1,column = 1,sticky = W)
        self.lab3 = Label(frame,text = "电子邮件")  
        self.lab3.grid(row = 2,column = 0,sticky = W)  
        self.ent3 = Entry(frame)  
        self.ent3.grid(row = 2,column = 1,sticky = W)
        self.lab4 = Label(frame,text = "手机号")  
        self.lab4.grid(row = 3,column = 0,sticky = W)  
        self.ent4 = Entry(frame)  
        self.ent4.grid(row = 3,column = 1,sticky = W)  
        self.lab5 = Label(frame,text = "",bg=top.cget('bg'))  
        self.lab5.grid(row = 4,column = 1)            #特殊预留文本框，颜色预设为背景色
        self.button = Button(frame,text = "提交",command = self.Submit)  
        self.button.grid(row = 5,column = 1)          
        #设置“提交”按钮键，点击时调用Submit函数
#分别针对不同需要输入的数据类型建立标签以及文本框，并针对它们的几何位置进行合理的调整

    def Submit(self):                                  #定义Submit函数
        data1=self.ent1.get()  
        data2=self.ent2.get()
        data3=self.ent3.get()
        data4=self.ent4.get() 
        #分别获得用户输入的数据
        if len(data1)==0 or len(data2)==0 or len(data3)==0 or len(data4)==0:
            self.lab5["text"] ='有项目未填写！'
            self.lab5["bg"]='red'
        #在有未输入的数据时，在预留文本框中显示“有项目未填写”，并将文本框背景改为红色
        else:
            print('新注册了一个用户：')
            print('用户名是：',data1)
            print('密码是：',data2)
            print('电子邮件地址是：',data3)
            print('手机号是：',data4)  
            self.ent1.delete(0,len(data1))  
            self.ent2.delete(0,len(data2))
            self.ent3.delete(0,len(data3))
            self.ent4.delete(0,len(data4)) 
            #在数据完全时，清空文本框中数据，并按要求显示