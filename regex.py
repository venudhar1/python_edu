import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

print('*' * 20)

my_str1='Hello buddy'
#        012345678910
print (my_str1[0:6])
print (my_str1[6:])

