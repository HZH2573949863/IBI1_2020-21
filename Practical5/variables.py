a=020208
b=190784
c=210310
d= abs(a-c)
e= abs(a-b)
if d < e:
 print ("d<e")
elif d > e:
 print ("d>e")
else:
 print ("d=e")
x=(4>0)
y=(2>5)
z=(x and not y)or(y and not x)
w=(x!=y)
print (z)
print (w)
