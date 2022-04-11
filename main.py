import math

input_numbers = input()

n = int(input_numbers.split(' ')[0])
k = int(input_numbers.split(' ')[1])

def newton_symbol(n : int,k : int) -> int :
    return int(math.factorial(n)/(math.factorial(k)* math.factorial(n-k)))

print(newton_symbol(n,k))
