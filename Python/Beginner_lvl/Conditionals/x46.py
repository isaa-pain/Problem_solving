#Description:
#1-Write a Python program that prints a descriptive message indicating if each
# character in a string is a vowel or a consonant. For example: "<char> is a <consonant | vowel>"
#2-If the character is a special character, number, or symbol, print "<char> is not a letter".
#3-If the string is empty, print "Empty String".
import string

string_a="Chaos:69"
dict_b={
        'vowel':'aeoiuy',
        'punctuation':string.punctuation+string.digits}
print(dict_b)
if not string_a:
    print("Empty String")
else:
    for i in string_a.lower():
        if i in dict_b['vowel']:
            print("<{form}> vowel".format(form=i))
        elif i in dict_b['punctuation']:
            print("<{form}> not a letter".format(form=i))
        else:
            print('<{form}> consonant'.format(form=i))
