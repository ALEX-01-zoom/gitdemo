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