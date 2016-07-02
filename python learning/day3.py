# def question(answer):
#     if answer == '42':
#         print('you are correct!')
#     else:
#         print('Nope, try again!')
#
# ans = input('What is the meaning of everything?')
#
# question(ans)
#
# def addNumber(x,y):
#     print(x + y)
#
# addNumber(55,99)
#
# def subNumber(x,y):
#     print(x - y)
#
# subNumber(33,31)
#
# def getBiggerNumber(x,y):
#     if x > y:
#         print(x)
#     else:
#         print(y)
#
# getBiggerNumber(3,5)
#
#
# def getSumOfLastDigits(lst):
#     last_digits = []
#     for item in lst:
#         str_item = str(item)
#         last_digits.append(int(str_item[-1]))
#         print(sum(last_digits))
#
# getSumOfLastDigits([12343, 1234567, 1324567890])
#
# def greeting(name, greet="Hello"):
#     print('{g} {n}!'.format(g=greet, n=name))
#
# greeting('Jash', 'YO')
#
# def addition(x, y):
#     return(x + y)
#
# ans = addition(5,5)
# other_ans = addition(10,10)
#
# print(addition(ans, other_ans))
#
# def isEquilateral(x,y,z):
#     return(x == y == z)
#
# print(isEquilateral(30, 30, 30))
#
#
# def addFirstAndLast(x):
#     last_digits = x[-1]
#     return x[0] + x[-1]
# print(addFirstAndLast([3,4,5]))
#
# def isEven(number):
#     if number % 2 == 0:
#         print(True)
#     else:
#         print(False)
# isEven(1)

def countA(word):
    print(word.count('a'))

print(countA("Jash"))
