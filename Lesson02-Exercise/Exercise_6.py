def carbon_foot(n):
    def action(x): 
        return x * n 
    return action

f = carbon_foot(100) 
print(f(0.03))
print(f(0.24)) 
print(f(0.06))