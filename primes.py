def check_for_prime(number):

    flag = False

    if number == 1:
        print(number, "is not a prime numberber")
    elif number > 1:
        # check for factors
        for i in range(2, int(number/2) + 1):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")


if __name__ == "__main__":

    check_for_prime(10) # calling the function