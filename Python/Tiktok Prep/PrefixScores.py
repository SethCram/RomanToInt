#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Sample Input:
# 4      →  n = 4 
# 5      →  arr = [5, 1, 4, 2]
# 1
# 4
# 2

import copy
import numpy as np

def getPrefixScores(arr):
    # Write your code here
    
    arrLen = len(arr)
    
    scoreArr = np.empty(arrLen, dtype=int)
    
    prevMax = None
    
    for i in range(arrLen):
        
        prefixArr = copy.deepcopy(arr[:i+1]) #arr slicing exclusive
        
        prefixArrMax = max(prefixArr)
        
        #if prev max not set or this prefix arr max isn't the same as last
        if i == 0 or prefixArrMax != prevMax:
            
            prefixArrLen = len(prefixArr)
            
            #recalc all the prefix sums
            for j in range(prefixArrLen):
                
                if j == 0:
                    prefixSum = prefixArrMax
                else:
                    prefixSum = copy.deepcopy( prefixArr[j-1] )
                
                prefixArr[j] += prefixSum
                
                if j == prefixArrLen - 1:
                    lastPrefixArrSum = copy.deepcopy( prefixArr[j] )
            
            prevMax = prefixArrMax
            
            scoreArr[i] = sum(prefixArr) % (10**9 + 7)
        #if max is the same as last max
        else:
            lastPrefixArrSum += prefixArr[-1]
            
            #only update score to account for new last value 
            scoreArr[i] = (scoreArr[i-1] + lastPrefixArrSum) % (10**9 + 7)
            
        print(prefixArr)
            
    return scoreArr
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getPrefixScores(arr)
    
    print('\n'.join(map(str, result)))

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
