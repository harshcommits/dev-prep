'''
difference between keyword and positional arguments needs to be clear
keyword arguments need to be mentioned first, and then positional arguments come into play
'''

def performOperation(num1, num2, operation="sum"):   # setting up the default value for a parameter
    if operation == "sum":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    else:
        return "Operation specified is invalid"
    
# for multiple args; only works for positional arguments
def multipleArgs(*args):
    print("Printing the list of args")
    for arg in args:
        print(arg)

# example for kwargs; handling keyword arguments as well
def kwargsfunc()
    
if __name__ == "__main__":
    print(performOperation(2, 4))   # takes sum operation by default, since no value is mentioned
    print(performOperation(2, 4, "multiply")) # when a specific value is given for operation, it takes action as per line 4

    # check for multiple args
    multipleArgs(1, 3, 5)