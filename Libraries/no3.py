import math
#QN 3
n = int(input('Enter a number:'))
factors = list(range(1,n + 1))

smallest_multiple = math.prod(factors)

print(factors)
print(smallest_multiple)
