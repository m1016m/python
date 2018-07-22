def f(a , b):
    a , b = b , a
    return a , b
a=1
b=2
(a, b) = f(a, b)
print ("a = ", a , ", b = " , b)