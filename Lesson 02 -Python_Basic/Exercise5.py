def prime_ans(num):
    a=2
    while a<num:
        if num%a==0:
            return False
            break
        a+=1
    if num==1:return False
    return True

prime=[]
for i in range(1,51):
    if prime_ans(i)==True:
        prime.append(i)
print (prime)
