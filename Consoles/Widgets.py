
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

class Text(Compos):
    """文字"""
    def __init__(self,console,text=""):
        self.text = text
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Text",{"text":text},[0,0]])

class HrefLine(Compos):
    """分割线"""
    def __init__(self,console):
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["HrefLine",[{}],[0,0]])

class Button(Compos):
    def __init__(self,console,text="",func=None):
        self.text = text
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Button",
                                     {"text":text,"function":func},
                                     [0,0]])

class Label(Compos):
    def __init__(self,console,fill="",width=0,height=0):
        self.fill=fill
        self.console = console
        self.number = len(self.console.widgets)
        self.console.widgets.append(["Label",
                                     {"fill":fill,"width":width,"height":height},
                                     [0,0]])

def configure(console,widget,config):
    console.widgets[widget.number][str(config)] = config