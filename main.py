x,y,l,d=input().split()
l=int(l)
x=int(x)
y=int(y)
d=int(d)
for i in range(0,y): # 输出图书馆
    for j in range(0,x):
        print('*',end='')
    print()
for i in range(0,l): # 输出电缆
    for j in range(0,d): # 输出电缆左边距
        print(' ',end='')
    print('|')
