def check_function_parameters(num1, num2, operation="sum"): # default value for an operation key
    if operation == "sum":
        print(num1 + num2) 
    else:
        print(num1 * num2)

if __name__ == "__main__":
    check_function_parameters(2, 4)
    check_function_parameters(2, 4, "multiply")