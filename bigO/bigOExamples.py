# O(1) Constant
def func_constant(values):
    print(values[0])
func_constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# O(n) Linear
def func_linear(list):
    for val in list:
        print(val, end=' ')
    print()
func_linear([1, 2, 3])

# O(n^2) Quadratic
def func_quadratic(list1, list2):
    for i in list1:
        for j in list2:
            print(i, '-', j, end=' ')
        print('|', end='')
func_quadratic([1,2,3,4], [1,2,3,4])

