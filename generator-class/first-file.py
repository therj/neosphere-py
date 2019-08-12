# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1


# x = countdown(5)

# print(x)


class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result


x = (PowTwo(2))

# for a in x:
#     print(a)


def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


x = PowTwoGen(8)
for i in x:
    print(i)
