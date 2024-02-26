# Console
应该可能是给控制台窗口用的库

----

# How to use?

example.py
```python
#py3
import Consoles as c

window = c.Console()
text = c.Label(window, fill=rgb(3,3,255,1)) #添加Label
line = c.HrefLine(a)
line.pack('center') #居中
window.EventLoop()
```
以上是一小段示例

__Label()__ 是其中的一个控件,用于创建一个Label对象.

__rgb()__ 函数可返回对应色值的ANSI转义序列

利用 __pack()__ 方法将其添加到屏幕上

其实这东东我还没弄好什么时候来个文档...

----

# TODO List
- 按钮事件绑定
- 鼠标/键盘窗口交互
- 在线文档
