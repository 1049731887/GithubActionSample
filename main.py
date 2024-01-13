h,x,y=input().split()
h=int(h)
x=int(x)
y=int(y)
for i in range(0,h):
    print('*',end='')
    if i==0 or i==y-1:
        for j in range(0,x-1):
            print('*',end='')
    elif i<y:
        for j in range(0,x-2):
            print(' ',end='')
        print('*',end='')
    print()
