# sum for 1+2+3+...+10
def f(n):
    print('n:',n) # Trace recursive levels
    if n==1:
        return 1 
    else:
        return n*f(n-1)

print('answer: ',f(10))