# O(log n) example using recursion function to make fibonacci
def fibo(n):
    seq = [0,1]

    for i in range(2,n+1):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return seq

seq = fibo(10)
print(seq)
print("Total = {0}".format(sum(seq)))
