编程题：
1、给定第y年第d天，写函数返回y年m月n日
lis1 = [31,28,31,30,31,30,31,31,30,31,30,31]
lis2 = [31,29,31,30,31,30,31,31,30,31,30,31]
def func(y,d):  # y年第d天
    if y % 4:  #判断是否为闰年，能整除为闰年且只有29天
        lis = lis1
    else:
        lis = lis2
        
    j = 0
    sm = 0
    while sm < d:
        sm = sm + lis[j]
        j = j + 1
    m = j
    n = d - sum(lis[0:j-1])
    return '%s年%s月%s日' %(y,m,n)

print(func(2019,2))
print(func(2019,345))
print(func(2008,23))
    
