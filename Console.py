import random,win32gui,os,time

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
        
        self.screen = []
        for i in range(0,self.height):
            self.screen.append(" "*self.width)
        self.widgets = [] #控件列表
    #打印屏幕
    def blit(self):
        #解析
        for widget in self.widgets:
            if widget[0] == "HrefLine":
                for i in range(0,self.height):
                    self.screen[i] = distract(self.screen[i],"|",widget[1][0])
            if widget[0] == "Text":
                self.screen[widget[2][1]] = distract(self.screen[widget[2][1]],widget[1],widget[2][0])
        print('\r' +'\n'.join(self.screen),end='')
        print('\033[{}A\033[{}D'.format(self.height,self.width), end='')#回到首行
    
    def GetWindowRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        return (left,top,right,bottom)

    def SetGeometry(self,width,height,x,y):
        pass

class Text():
    """文字"""
    def __init__(self,console,text):
        self.text = text
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Text",[text]])
    def pack(self,x=0,y=0):
        self.x = x
        self.y = y    
        self.console.widgets[self.number].append([x,y])
        self.console.blit()

class HrefLine():
    """分割线"""
    def __init__(self,console):
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["HrefLine"])
    def pack(self,x):
        self.x = x
        self.console.widgets[self.number].append([x])
        self.console.blit()

def rgb(r=0,g=0,b=0,bgcolor=False):
    """返回真彩色ANSI控制符
    r,g,b:色值
    bgcolor:是否设置背景颜色
    """
    if bgcolor:
        bgcolor=48
    else:
        bgcolor=38
    return "\033[{};2;{};{};{}m".format(bgcolor,r,g,b)

def distract(fststr,secstr,start=0):
    """字符串插入
    fststr:要被插入的字符串
    secstr:要插入的字符串
    start:起始字符串位置
    """
    
    fststr=list(fststr)
    for i in range(0,len(secstr)):
        fststr[start+i] = secstr[i]
    return "".join(fststr)
