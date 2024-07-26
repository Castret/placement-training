
a = 900
b = 1000

print("Prime numbers between",a, "and", b, "are:")

for num in range(a, b + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
