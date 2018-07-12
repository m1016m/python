#練習1
moneyA = 91 
hrA = 20
moneyB = 75
hrB = 15
moneyC = 60
hrC = 25
if moneyA > 90 :
    A=hrA*200
    Am=A+8000
    print "A月薪:",Am

if moneyB >=70 and moneyB <=90 :
    B=hrB*200
    Bm=B+6000
    print "B月薪:",Bm

if moneyC < 70 :
    C=hrC*200
    Cm=C+4000
    print "C月薪:",Cm

#練習2

moneyD = 75 
hrD = 10
moneyE = 80
hrE = 12
moneyF = 90
hrF = 25
if moneyE >=70 and moneyE <=90 :
    E=hrE*200
    Em=E+6000
    print "E月薪:",Em

if moneyD >=70 and moneyD <=90 :
    D=hrD*200
    Dm=D+6000
    print "D月薪:",Dm

if moneyF >= 90 :
    F=hrF*200
    Fm=F+4000
    print "F月薪:",Fm

#練習3
moneyD = 75 
hrD = 10
moneyE = 80
hrE = 12
moneyF = 90
hrF = 25
if moneyE >=70 and moneyE <=90 :
    E=hrE*200
    Em=E+6000
    print "E月薪:",Em

if moneyD >=70 and moneyD <=90 :
    D=hrD*200
    Dm=D+6000
    print "D月薪:",Dm

if moneyF >= 90 :
    F=hrF*200
    Fm=F+4000
    print "F月薪:",Fm
#練習4
def f(money , hr):
    if money >=90:
         print "月薪:",8000+hr*200
    elif money <= 89 and money >= 60 : 
         print "月薪:",6000+hr*200
    else:
        print "月薪:",4000+hr*200 

f(55 ,14)
f(96 , 13)
f(85 , 22)

def f(n):
    if n <= 0:
        return 
    else:
        row = [1]
        for i in range(10):
            print row 
            p = row[:] 
            for j in range(1, len(row)):        
                row[j] = p[j] + p[j-1]
            row.append(1)


f(10)
for i in range(4):         # 總共有4層
        for j in range(4 -i - 1): # 在第一個*號出現前，先印出空白
                 print " ", 
        for k in range(i + 1):                # 印出該層所需要的*字數量
                print "* ",
        print ""                # 換行


