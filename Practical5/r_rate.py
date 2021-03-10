# I want to create a function called num(n), which equals to the number of infected individuals after n rounds of infection.
r = 2 # Firstly, defineate r as a seperate variable.
def num(n):
 if n <= 1:
  v = 84 # v is the value of num(n).
  return v
 else:
  v = num(n-1) * r
  return v
print (num(6)) # Because after 5 infections, the number should be num(6).
