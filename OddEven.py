#O(1) example using  if else to identify odd or even number
num = int (input("Enter a number: "))

if(num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
