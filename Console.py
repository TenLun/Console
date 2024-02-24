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
        self.colors = [] #颜色 [ansi,x,y,length]
        self.screen = NullList([], NullList([], ["", ""], self.width), self.height) #最终输出的屏幕,四维数组
        # 1st dimension: each row
        # 2nd dimension: each glyphs
        # 3rd dimension: the unicode(? of the glyph and its color [uni,color]
        

        
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
                for i in range(0,self.height):
                    self.screen[i][x][0] ="|"
            elif name == "Text":
                self.screen[y][x][0] = options["text"]
            elif name == "Button":
                pass
            elif name == "Label":
                for i in range(0,options["height"]):
                    self.colors.append([options["fill"],x,y+i,options["width"]])

        #颜色(重构ing)
        
        #os.system("cls")#回到首行
        print('\033[{}A\033[{}D'.format(self.height*2,self.width*2), end='')

        print('\r' +'\n'.join(MergeList(self.screen, 1)),end='')
    
    def GetWindowRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        return (left,top,right,bottom)

    def SetGeometry(self,width,height,x,y):
        pass

    def ScreenReset(self):
        self.screen = []
        for i in range(0,self.height):
            self.screen.append(" "*self.width)
    def EventLoop(self):
        #更新窗口大小
        while 1:
            if self.width != os.get_terminal_size().columns or self.height != os.get_terminal_size().lines:
                try:
                    self.width = os.get_terminal_size().columns
                    self.height = os.get_terminal_size().lines
                except:
                    pass
                Console.ScreenReset(self)
                Console.blit(self)