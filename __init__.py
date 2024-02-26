import random,win32gui,os
from .StrTools import *
from .Widgets import *

class Console():
    def __init__(self):
        #get hwnd
        self.number = int(random.random()*10**16)
        os.system("title {}".format(self.number))
        self.hwnd = win32gui.FindWindow(None,"{}".format(self.number))
        while self.hwnd == 0:
            self.hwnd = win32gui.FindWindow(None,"{}".format(self.number))
        #init
        self.width = os.get_terminal_size().columns
        self.height = os.get_terminal_size().lines

        
        self.widgets = [] #控件列表 [name,options,position]
        self.colors = [] #颜色 二维列表 [ansi,x,y,length]
        self.screen = [] #最终输出的屏幕,三维列表
        # 1st dimension: each row
        # 2nd dimension: each glyphs
        # 3rd dimension: the unicode(? of the glyph and its color [color, uni]
        self.ScreenReset()
        

        
    #打印屏幕
    def blit(self):
        #解析(内存爆炸)

        #组件
        for widget in self.widgets:
            name, options, position = widget
            #pack
            if position == ["center"]:
                x = int(self.width/2)
                y = int(self.height/2)
            else:
                x,y = position
            #widgets
            if name == "HrefLine":
                for i in range(self.height):
                    self.screen[i][x][1] ="|"
            elif name == "Button":
                pass
            elif name == "Label":
                for text in options["text"]:
                    self.screen[y][x][1] = text
                for i in range(options["height"]):
                    self.colors.append([options["fill"],x,y+i,options["width"]])

        #颜色
        for color in self.colors:
            name, x, y, length = color
            for i in range(length):
                self.screen[y][x+i][0] = name
        
        #返回首行
        print('\033[{}A\033[{}D'.format(self.height*2,self.width*2), end='')

        print('\r' +'\n'.join(MergeList(self.screen)),end='')
    
    def GetWindowRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        return (left,top,right,bottom)

    def SetGeometry(self,width,height,x,y):
        pass

    def ScreenReset(self):
        self.screen = [[["\033[0m", "\x20"] for i in range(self.width)] for i in range(self.height)]
        
    def EventLoop(self):
        """事件循环"""
        Console.ScreenReset(self)
        Console.blit(self)
        #更新窗口大小
        while 1:
            if self.width != os.get_terminal_size().columns or self.height != os.get_terminal_size().lines:
                try:
                    self.width = os.get_terminal_size().columns
                    self.height = os.get_terminal_size().lines
                except:
                    pass
                os.system("cls")#回到首行
                Console.ScreenReset(self)
                Console.blit(self)
