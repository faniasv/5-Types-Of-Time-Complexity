#O(2^n) example using subset arrays

# function to generate sub lists
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
 
# input
ar = [1, 2, 3]
print(sub_lists(ar))