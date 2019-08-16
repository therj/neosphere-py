import sys


def test_fun(args):
    print(args[1])
    print(args[2])


if __name__ == '__main__':
    test_fun(sys.argv)
