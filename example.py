"""
os.system('cls')
#os.get_terminal_size()
screen=[]

def ScreenReset():
    global screen
    screen=[]
    for i in range(0,30):
        screen.append(" "*120)

def plit(width,height):
    print('\r' +'\n'.join(screen),end='')
    print('\033[{}A\033[{}D'.format(height,width), end='')#回到首行

def distract(fststr,secstr,start=0):
    ""字符串插入
    fststr:要被插入的字符串
    secstr:要插入的字符串
    start:起始字符串位置
    ""
    
    fststr=list(fststr)
    for i in range(0,len(secstr)):
        fststr[start+i] = secstr[i]
    return "".join(fststr)

class Text():
    def __init__(self,text):
        global screen
        self.text = text
        screen[0] = distract(screen[0],text)

class HrefLine():
    def __init__(self,x):
        global screen
        self.x = x
        for i in range(0,30):
            screen[i] = distract(screen[i],"|",x)


ScreenReset()
print(rgb(120,3,31,1),end='')
a = Text('hello')
ad = HrefLine(3)
plit(120,30)
os.system('pause') #debug


print('\033[0;31;42m',end='')

plit(120,30)
print('\033[3A', end='')  # cursor up 5 lines
print('\r', end='')  # cursor back to start
print('\033[0J', end='')  # erase from cursor to end


print('\rhello',end='')
os.system('pause')
#预想用数组
#screen = [" "*width,.....," "*width]
#screen[1][2]
#输出是
#screen = screen.join('\n')

"""
import os
from Console import *

a = Console()
c = HrefLine(a)
c.pack('center')
a.EventLoop()
