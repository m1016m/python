def maker(n):
    def action(x): # Generate and return action
        return x ** n # action retains N from enclosing scope return action
    return action

f = maker(5) # Pass 2 to argument N
print(f(9))
print(f(3)) # Pass 3 to X, N remembers 2: 3*2=6
print(f(4))

def func(x, y, z):
    return lambda x,y,z : x+y+z


func2 = func(1, 2, 3)
print (func2(1,2,3))

def math_fuc(n):
    result = 0
    if n == 1:
        result = 1
    else:
        result = n *math_fuc(n-1)
    return result

for i in range (1 , 20):
    print "i = %d " % i,
    print (math_fuc(i))


