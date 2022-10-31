#A program to check if a given int is a palindrome

def isPalindrome(x):
    num = str(x)
    rev = num[::-1]
    if num == rev:
        return True
    else:
        return False
        
print(isPalindrome(222))