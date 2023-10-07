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
        self.widgets = [] #控件列表 [name,options,position]
        self.colors = [] #颜色 [ansi,x,y,length]
        self.screen = []
        for i in range(0,self.height):
            self.screen.append(" "*self.width)
        
    #打印屏幕
    def blit(self):
        #解析
        for widget in self.widgets:
            name = widget[0]
            content = widget[1]
            #pack
            if widget[2] == ["center"]:
                x = int(self.width/2)
                y = int(self.height/2)
            else:
                x,y = widget[2]

            if name == "HrefLine":
                for i in range(0,self.height):
                    self.screen[i] = StrDistract(self.screen[i],"|",x)
            elif name == "Text":
                try:
                    self.screen[y] = StrDistract(self.screen[y],content[0]["text"],x)
                except:
                    pass
        os.system("cls")
        for color in self.colors:
            self.screen[color[2]] = StrReplace(self.screen[color[2]],color[0],color[1])
            self.screen[color[2]] = StrReplace(self.screen[color[2]],"/033[0m",color[1]+color[3])
            
        print('\033[{}A\033[{}D'.format(self.height*2,self.width*2), end='')#回到首行
        print('\r' +'\n'.join(self.screen),end='')
    
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
        while 1:
            if self.width != os.get_terminal_size().columns:
                self.width = os.get_terminal_size().columns
                Console.ScreenReset(self)
                Console.blit(self)
            if self.height != os.get_terminal_size().lines:
                self.height = os.get_terminal_size().lines
                Console.ScreenReset(self)
                Console.blit(self)

class Compos():
    def pack(self,direction):
        self.direction = direction
        self.console.widgets[self.number][2] = [self.direction]
        self.console.blit()

    def place(self,x,y=0):
        self.x = x
        self.y = y    
        self.console.widgets[self.number][2] = [x,y]
        self.console.blit()

class Text(Compos):
    """文字"""
    def __init__(self,console,text):
        self.text = text
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Text",[{"text":text}],[0,0]])

class HrefLine(Compos):
    """分割线"""
    def __init__(self,console):
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["HrefLine",[{}],[0,0]])

def StrDistract(fststr,secstr,start=0):
    """字符串替换
    fststr:要被插入的字符串
    secstr:要插入的字符串
    start:起始字符串位置
    """
    
    fststr=list(fststr)
    for i in range(0,len(secstr)):
        fststr[start+i] = secstr[i]
    return "".join(fststr)

def StrReplace(fststr,secstr,start=0):
    """字符串替换
    fststr:要被插入的字符串
    secstr:要插入的字符串
    start:起始字符串位置
    """
    fststr = list(fststr)
    fststr.insert(start,secstr)
    return "".join(fststr)

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
