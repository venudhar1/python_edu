from coverage.files import sep

x_i = 123  # integer
x_j = 123L  # long integer
x_k = 3.14  # double float
x_l = "hello"  # string
x_m = [0, 1, 2]  # list
x_n = (0, 1, 2)  # tuple

print x_i
print x_j
print x_k
print x_l
print x_m
print x_n

# =============

print("Test_new\
_line")
print("Test_new_line")
# =============

a \
    = \
    10
print(a)

# =============

print("""Hi
how are you?""")


# =============

# Below Gives ERROR :
#
# """b\
# =\
# 10"""
# print(b)
# =============

def greet_func():
    """
    This function prints out a greeting
    """
    print("Hi")
print "==========="


greet_func()
# =============

if 2 > 1:
    print("2 is the bigger person");
    print("But 1 is worthy too");

#if 2 > 1:
#    print("2 is the bigger person");
#      print("But 1 is worthy too");
# The above will give error space/identation is very strict

# =============
print "==========="

a=7;print(a);
type(a);

print('We need a chaperone');
print("We need a 'chaperone'");
#print("We need a "chaperone"");   This will give error
print("We need a \"chaperone\"");

#test
print "gitworkouttest"
# =============
print "==========="

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print a

ab = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print ab

colors = ['red',
          'blue',
          'green']
print colors

print ('est_\
we')
print "==========="

for i in range(1,11):
    print(i)
    if i == 5:
        break

def double(num):
    """Function to double the value"""
    return 2*num

print double(17)
print "==========="

website = "apple.com"
print (website)
print('website')     # wrong way
print("website")     # wrong way. It will treate '' and "" as non-variables
print website
print "==========="
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

# print("Hello", "how are you?", sep="---")     # python 3.x has sep which can saparate the prints values # output is Hello --- How are yoy?
# print('G','F','G', sep='')                Output is GFG

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"     # Unicode String literal
raw_str = r"raw \n @#$%Z^Zstring"  # Byte String literal

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
print "==========="

#Boolean srings

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + True + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


print False and True #False
print False or True #True
print False or False #False
print True or True #True
print False and False #False
print True and True #True
print True or False #True
print True and False #False
print "==========="

my_string = "Hello World"

print my_string.isalnum()		#check if all char are numbers
print my_string.isalpha()		#check if all char in the string are alphabetic
print my_string.isdigit()		#test if string contains digits
print my_string.istitle()		#test if string contains title words
print my_string.isupper()		#test if string contains upper case
print my_string.islower()		#test if string contains lower case
print my_string.isspace()		#test if string contains spaces
print my_string.endswith('d')	#test if string endswith a d
print my_string.startswith('H')	#test if string startswith H

print my_string[3:7]  #[H e l l o   W o r l d ]   output is "lo W"
                      #[0 1 2 3 4 5 6 7 8 9 10]

print "==========="
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
print text
# Split the line into chunks, which are concatenated automatically by Python
text = (
        "%d little pigs come out, "
        "or I'll %s, and I'll %s, "
        "and I'll blow your %s down."
        % (3, 'huff', 'puff', 'house'))
print text
print "==========="

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alpha_tuple=('a', 'b', 'c')
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(alphabets['b'])
print(vowels)
print alpha_tuple
print "==========="

"""

Python Collections (Arrays)::
There are four collection data types in the Python programming language:

1)LIST is a collection which is ordered and changeable. Allows duplicate members.
2)TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
3)SET is a collection which is unordered and unindexed. No duplicate members.
4)DICTIONARY is a collection which is unordered, changeable and indexed. No duplicate members.

"""