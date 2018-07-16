def maker(n):
     return lambda x: x ** n
    
h = maker(5)
print(h(9))