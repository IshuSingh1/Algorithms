#Normal
def sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
print("Normal sum", sum(5))

#Using a Formula
def sum2(n):
    return(n*(n+1)/2)
print("Formula sum", sum2(5))