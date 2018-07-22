def MxM_multiplication(m) :
    for i in range(1,m) :
        for j in range(1,m) :
            print (i , "*" , j , "=" ,(i*j),end = "\t")
        print ("")


MxM_multiplication(9)