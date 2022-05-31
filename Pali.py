word = str( input('Enter a word to verify if is a palindrome:'))
if str(word) == str(word)[::-1] :
    print("It is a Palindrome")
else:
    print("Not Palindrome")