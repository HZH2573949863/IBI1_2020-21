def fibonacci(n): # create a function called fibonacci(n)
# create a system that will make the circulation happen 
 if n <= 2:
  v = 1
  return v
 else:
  v = fibonacci(n-1) + fibonacci(n-2)
  return v
for i in range(1,14): # start to print the result of the function
 print (fibonacci(i))
