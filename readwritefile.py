my_strin = "Hello! Welcome to demofile.txt\n\
This file is for testing purposes.\n\
Good Luck! \n"
filePath = '/etc/nsswitch.conf'
#method 1

with open(filePath, 'r') as f:
    for line in f.readlines():
        print(line)
print "==========="
#method 2
#with open('/etc/nsswitch.conf', 'r') as f:


f = open('/tmp/python_write_test', 'w')
f.write(my_strin)
f.close()

with open('/tmp/python_write_test', 'r') as f:
    print(f.read())
    print "==========="

#read, readline, readlines, write, writelines
#r-read,w-write,a-append