'''
the following code snippets detail out the variable scopes in different scenarios, and relevant implementations
'''

# check for local variables; returns a dictionary of all variables as key-value pairs
def localCheck(num1, num2, operation='sum'):
    print(locals())


if __name__ == "__main__":
    localCheck(1, 3, 'multiply')