# Console
应该可能是给控制台窗口用的库

----

# 怎么用？/How to use?

```python
#py3
import Console.Console as c

window = c.Console()
window.colors.append([c.rgb(3,3,255,1),3,3,3]) #添加屏幕背景颜色
text = c.Text(a,'hello')
line = c.HrefLine(a)
line.pack('center') #居中
window.EventLoop()
```
以上是一小段示例

__Text()__ 是其中的一个控件,用于创建一个文本对象.

利用 __pack()__ 方法将其添加到屏幕上

__rgb()__ 函数可返回对应色值的ANSI转义序列

<p style='font-size:1px'>其实这东东我还没弄好什么时候来个文档...</p>
