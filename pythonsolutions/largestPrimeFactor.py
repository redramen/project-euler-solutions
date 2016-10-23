"""
Question 3.
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def largestPrimeFactor():
    currentFactor = 2
    ourNum = 600851475143     # the number we are interested in, can turn into a parameter
                              # instead to generalize for any number

    while currentFactor * currentFactor <= ourNum:
        while ourNum % currentFactor == 0:         # is our number divisible by our factor that we are testing?
            ourNum //= currentFactor               # using '//' instead of '/' gives an integer instead of float
        currentFactor += 1                         # increment factor when the number is no longer divisble by it
    if ourNum > 1:
        return ourNum
    return currentFactor

print(largestPrimeFactor())
