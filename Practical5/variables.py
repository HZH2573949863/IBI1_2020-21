a="020208"
b="190784"
c="210310"
d= abs(int(a)-int(c))
e= abs(int(a)-int(b))
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
