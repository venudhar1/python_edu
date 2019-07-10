
for row in range(6):
    for col in range(7):
        if ((row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8)):
            print ("*"),
        else:
            print(" "),
    print



#strin1 = raw_input("Input word: ") #python
strin1 = "python"

length1 = len(strin1) #length1 is 6

for row1 in range(length1):
    for col1 in range(row1+1):
        print (strin1[col1]),
    print ("")


#strin2 = raw_input("Input number: ") #python

#n = int(strin2)

for i in range(1, 8, 2):
    print (i * '*')


for i in range(1,6):
    for j in range(1,(2*i)):
        print("*"),
    print