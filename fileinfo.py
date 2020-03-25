#17377156  朱奂璋
#GUI界面设计

from tkinter import *                                 #从tkinter库中导入*
class Reg (Frame):                                    #使用Frame方法（首先定义Reg类）
    def __init__(self,master):                        #定义__init__方法
        frame = Frame(master)                         #指定Frame中的父窗口为frame
        frame.pack()                                  #使用pack类