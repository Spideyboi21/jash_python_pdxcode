"""
Write a function that prints out a number to 100
but if that number is divisible by 3 instead of the number we print "Fizz"
if that number is divisible by 5 we print "Buzz"
and if that number is divisible by 5 and 3 we print "FizzBuzz"
"""

def fizzbuzz(n):
    nums = list(range(1, n+1))
    for num in nums:
        if num % 5 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print
# 2 % 3 == 0 / False
# 3 % 3 == 0 / False
