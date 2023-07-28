def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
def sum_inf(e = 0.0001):
    i = 1
    sum = pow(-1,i)/ factorial(i+1)
    while True:
        i += 1
        result = (pow(-1,i)/ factorial(i+1))
        if abs(result) < e:
            break
        sum += result
    return sum
    
print(sum_inf())

