a = -1
if a > 3:
  print ("a > 3")
elif a == 3:
  print ("a = 3")
else:
  print ("a < 3")
  

x, y, z = 3, 9, 6

x, y, z = z, x, y
if x < y > z:
  print("OK")

n1 = 5
n2 = 3
n3 = 6
if (n1 > n2):
	if(n1 > n3):
		print ("Big number:  %s",str(n1))
	elif(n2 > n3):
		print ("Big number:  %s",str(n2))
else :
	print ("Big number:  %s",str(n3))



a = True and True
b = True and False
c = False and False
d = True or True
e = True or False
f = False or False
g = not False
print (a, b, c, d, e, f, g)
