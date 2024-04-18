def check_for_palindrome(value):
    if value[::-1] == value:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

if __name__ == "__main__":
    string_for_checking = input("Enter the string to check for palindrome\n")
    check_for_palindrome(string_for_checking.lower())