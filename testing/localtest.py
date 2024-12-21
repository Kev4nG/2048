from operator import xor
from threading import local

#this is for shigtin
            #0 1 2 3
arr= [2,0,2,0]
length = len(arr) -1

count = 0 
# if local 
while count != length:
    left = arr[count]
    right= arr[count+1]

    if left == 0 and right != 0:
        left ^= right
        right ^= left
        left ^= right  

        arr[count] = left
        arr[count + 1] = right     

        count = 0

    count += 1

print(arr)