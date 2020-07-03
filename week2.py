In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
filename=input("enter file name")
fhand=open(filename)
sum=0
for line in fhand:
    line=line.strip()
    if(re.search('[0-9]+',line)):
        str=re.findall('[0-9]+',line)
        for s in str:
            sum+=int(s)
print(sum)
