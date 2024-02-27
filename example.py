import Consoles,random
from pyautogui import position
"""
b = Text(a,text="hello")
a.blit()
a.EventLoop()
"""

def sync(var):
    b.configure(a,b,"text","{}".format(var))

a = Consoles.Console()

b = Consoles.Label(a,width=2,height=1,text="hello")

a.AddFunc(lambda :sync(position()))

a.EventLoop()
