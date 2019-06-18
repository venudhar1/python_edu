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

a=7;print(a);
type(a);

print('We need a chaperone');
print("We need a 'chaperone'");
#print("We need a "chaperone"");   This will give error
print("We need a \"chaperone\"");

