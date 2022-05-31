num= int(input("What number do you want to know if is a prime? "))
value= range(2,num)
counter = 0
for n in value:
  if num % n == 0:
    counter +=1
    print("divisor:", n)
 
if counter > 0 :
  print("It is not a prime number" )
else:
  print("It is a prime number")