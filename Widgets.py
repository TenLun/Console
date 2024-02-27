
#放置 基类
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

    def configure(self,console,widget,config,var):
        self.console.widgets[widget.number][1][str(config)] = var

class HrefLine(Compos):
    """分割线"""
    def __init__(self,console):
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["HrefLine",{},[0,0]])

class Button(Compos):
    def __init__(self,console,text="",func=None):
        self.text,self.func = text,func
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Button",
                                     {"text":text,"function":func},
                                     [0,0]])

class Label(Compos):
    """文字"""
    def __init__(self,console,fill="",width=0,height=0,text="hello"):
        self.fill, self.width, self.height, self.text=  fill, width, height, text
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Label",
                                     {"fill":self.fill,"width":self.width,"height":self.height,"text":self.text},
                                     [0,0]])


