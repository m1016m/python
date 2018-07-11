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
