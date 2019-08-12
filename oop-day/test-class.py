# # # def optFun(a, b):
# # #     return (a+b, a*b, a/b)


# # # # lambda a, b: a*b

# # # # print(optFun(2, 3))

# # # def exampleFunction(x):
# # # return x


# # # def exampleFunctionLambda(x): return 5


# # # def testFun(parameter_list): return expression


# # def testFun(x=1, y=1):
# #     try:
# #         return x/y
# #     except:
# #         # print("Error")
# #         return "Nooo"


# # a, b = 2, 4
# # # print(2+"a")
# # print(f'{a}, {b} => {testFun(a)}')
# a = 1


# # def recFun():
# #     a += 1
# #     print(a)
# #     while a < 10:
# #         return recFun()


# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         # print("Function called!")
#         return x * factorial(x-1)


# # x = int(input("Enter a Number: "))
# # x = 3
# # print("Factorial of", x, "is: ", factorial(x))

# print(factorial(8))


class testClass():
    def __init__(self, nameVar, ageVar):
        print("name", nameVar)
        self.name = nameVar
        self.age = ageVar
        # print("age", age)
        print("Init called")
        # pass
    # def __init__(self, name):
    # self.name = name
    # self.age = age
    # print("init called")

    # def testFun(self):
    # print("testFun called")

    # roshan = testClass("Roshan")


roshan = testClass("Roshan", 22)
print(roshan.age)
print(roshan)
# sushant = testClass()
# print(roshan)
# sushant.testFun()

# print(test)
