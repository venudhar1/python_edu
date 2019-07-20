from sys import argv

def add(a,b):
    c = a + b
    print(c)

add(b=10,a=5)

def person(name,age):
    print("age of", name, "is", age)

person("venu",20)

def display(*cources):
    for i in cources:
        print(i),
display("one","two","three")

def collcources(name,cource="B.Tech"):
    print
    print(name)
    print(cource)

collcources("venu") # or collcources(name="venu",cource="BSC")
collcources("venu","BSC")


print(argv[0])
print(argv[1])
print(argv[2])
print(len(argv))
for g in argv:
    print(g)
print(argv)


# *args
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('venu','python','eggs','test')

# **kwargs
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)

greet_me(name = "venu")

# args and kwargs
def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3,5)
test_args_kwargs(*args)
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)