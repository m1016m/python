
def maker(n):
    def action(x): # Generate and return action
        return x * n # action retains N from enclosing scope return action
    return action

f = maker(2) # Pass 2 to argument N
g = maker(3) # Pass 3 to argument N

print(f)
print(f(4)) # Pass 4 to X, N remembers 2: 2*4=4

print(g)
print(g(4)) # Pass 4 to X, N remembers 3: 3*4=6