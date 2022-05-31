n=int(input("Enter the quantity of numbers that you want': "))
first=0
second=1
sum=0
count=1
print("Fibonacci Sequence: ")
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second	