def f(x):
    for i in range(2 , x):
        for j in range(1 , x):
            print i , "*" , j ,"=" ,i *j,"\t",
        print "\n"

f(9)