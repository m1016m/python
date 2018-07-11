import random
answer = random.randint(0 , 100)# 正確數字
guess = 0                   # 設定所猜數字的初始值
while guess != answer:
         guess = int(input("請猜1-100間的數字 = "))
         if guess > answer:
            print "請猜小一點"
            print "answer:" , answer
         elif guess < answer:
            print "請猜大一點"
            print "answer:" , answer
         else:
            print "恭喜答對了"
print ""

x = 10
for i in range(1, 10):
    x -= 1
    for j in range(1, x ):
        
        print "aa", 
    print ""

num = int(input("請輸入1~100的整數做質數測試 = "))
if num == 2:                                # 2是質數所以直接輸出
    print "%d是質數" % num
else:
    for n in range(2, num):                 # 用2 .. num-1當除數測試
        if num % n == 0:                    # 如果整除則不是質數
            print "%d不是質數" % num
            break                           # 離開迴圈

    else:                                   # 否則是質數
        print "%d是質數" % num


import math
def math_h(a,b,c):
    num=b**2-4*a*c
    if num < 0:
        raise ValueError,'it is invalid'
    kv=math.sqrt(num)
    return (-b+kv)/a/2,(-b-kv)/a/2

print math_h(1,-2,1)
print math_h(1,6,8)


def myline(startx,starty,endx,endy):
        for x in range(startx, endx):
                y=int((x-startx)*(endy-starty)/(endx-startx))+starty
                print "(x, y) = (%d, %d)" % (x, y)
 
myline(378,279,421,319)







