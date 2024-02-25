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
    secstr:要插入的
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


def MergeList(list) -> list:
    outList = []
    for firstElement in list:
        queueList = []
        for secondElement in firstElement:
            queueList.append(secondElement[0])
        outList.append("".join(queueList))
    return outList
    
