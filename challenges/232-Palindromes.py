import re

def isPalindrome(file):
    infile = open(file, 'r')
    lines = infile.readlines()

    num_lines = int(lines[0])
    total_string = "";

    for line in lines[1: (num_lines+1)]:
        total_string += line

    total_string = re.sub('[^a-zA-Z0-9]', '', total_string)
    total_string = total_string.lower()

    if(total_string == total_string[::-1]):
        print('Palindrome')
    else:
       print('Not a palindrome')


isPalindrome('../resources/long_palindrome.txt')
