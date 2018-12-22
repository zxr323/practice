2、给定ls,从ls中取3个数组成不重复3位数（重复取，不重复取）
ls = [1,2,3,4]
def func1(l):
    "重复取"
    lis1 = []
    for i in ls:
        for j in ls:
            for k in ls:
                lis1.append(str(i)+str(j)+str(k))
    return lis1
a = func1(ls)
print(a,len(a))
        
def func2(l):
    "不重复取"
    lis1 = []
    for i in ls:
        for j in ls:
            for k in ls:
                if i != j and i != k and j != k: #多的部分
                    lis1.append(str(i)+str(j)+str(k))
    return lis1
b = func2(ls)
print(b,len(b))
