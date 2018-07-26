from stack import Stack
def dec_to_bin(dec):
    s=Stack()
    cur=dec
    while cur>0:
        a=cur%2
        s.push(a)
        cur = cur // 2
    binstr=''
    while not s.isEmpty():
        binstr+=str(s.pop())
    return binstr

print (dec_to_bin(42))   # 回傳 101010
print (dec_to_bin(100))  # 回傳 1100100