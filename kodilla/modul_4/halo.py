import sys


def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))


if __name__ == "__main__":
    print(sys.argv)
    customized_hello("John", "Cleese")
