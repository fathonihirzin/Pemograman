def isPalindrome(number):
    return str(number) == ''.join(reversed(str(number)))

number = int(input("Enter number: "))

if isPalindrome(number):
    print("True")
else:
    print("False")