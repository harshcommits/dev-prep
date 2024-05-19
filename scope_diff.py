message = "Some global text for scoping"

varA = 2

def function1(varA, varB):
    print(varA)
    print(message)
    print(locals())

def function2(varC, varB):
    print(varA)
    print(message)
    print(locals())


if __name__ == "__main__":

    function1(1, 2) # prints message value, print varA as 1, since local variable value takes priority
    function2(3, 4) # prints message since it's global, prints varA as 2 since there is no local definition and global value is 2