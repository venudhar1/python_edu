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

#open a file, read the nth and add the nth column number

with open('FL_insurance_sample.csv', 'r') as f:
    n = 0
    for line in f.readlines():
        if "CLAY" in line:
            n += float(line.split(',')[7])
    print n



lines = open('C2ImportCalEventSample.csv', 'r')
for line in lines:
    if "Social" in line:
        print line.split(',')[7][0]                             # 7th field and 0th char of the 7th field  = 'A'pple
        fields = line.split(',')
        print(fields[7], fields[8])
