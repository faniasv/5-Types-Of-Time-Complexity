#O(n) example using sort function to sort array of numbers
num = [2,5,8,0,3,10,6]

max = num[0]

for x in num:
    if x > max:
        max = x

print(max)
