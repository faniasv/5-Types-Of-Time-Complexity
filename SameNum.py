#O(n^2) example using nested loop to sort same numbers
for i in range (4):
    for j in range(4):
        if j == i:
            break
        print(i,j)