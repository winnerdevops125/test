for _ in range(int(input())):
    h,c,t=map(float,input().split())
    if h>50 and c<0.7 and t>5600:
        print(10)
    elif h>50 and c<0.7:
        print(9)
    elif c<0.7 and t>5600:
        print(8)
    elif h>50 and t>5600:
        print(7)
    elif h>50 or c<0.7 or t>5600:
        print(6)
    elif not h>50 and not c<0.7 and not t>5600:
        print(5)