def maker( n ) :
    def action ( x) :
        return n ** x
    return action



f = maker(9)
print(f(5))  #59049 (為9的5次方)