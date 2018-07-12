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