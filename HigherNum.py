#O(n) example using sort function to sort array of numbers
num = [2,5,8,0,3,10,6]
num.sort()

print(num)

print("without built in function")
new_num = []
while num:
    min = num[0]  
    for x in num: 
        if x < min:
            min = x
    new_num.append(min)
    num.remove(min)    

print(new_num)
