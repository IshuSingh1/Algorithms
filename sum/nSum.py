import time

# Brute Force
def sum1(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# Formula
def sum2(n):
    return(n*(n+1)/2)


n = 100000

start = time.time()
sum = sum1(n)
end = time.time()
print("Sum1 sum", sum, "in", (end-start))

start = time.time()
sum = sum2(n)
end = time.time()
print("Sum2 sum", sum, "in", (end-start))
