"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

def evenFibSum():
    fibSum = 0
    a, b = 1, 2             # sets a to 1, b to 2

    while a <= 4000000:     # while the value of the fib num does not exceed 4 mil.
        if a % 2 == 0:      # checking that the value is even,
            fibSum += a     # if so, we add it to our sum.
        a, b = b, a + b     # this line calculates the fibonacci number
    return fibSum


print(evenFibSum())
