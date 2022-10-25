#Usage python md5Covert.py <filename.txt>

import hashlib
import sys

#Conversion Function using Hashlib
def convertToMd5(str):
    
    return hashlib.md5(str.encode('utf-8')).hexdigest()
   

#Using sys to read file, and store in array
with open(sys.argv[1], 'r') as list:
    array = list.readlines()
 

lengthOfList = len(array)


res = []
#Removing \n from original file, \n is added as a result of the .readlines() fuction
for sub in array:
    res.append(sub.replace("\n", ""))

#Iterating through all elements within text file. 
for x in range(lengthOfList):
    hash = str(res[x])
    print(convertToMd5(hash)) 
