#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    numSwaps = 0
    for i in range(n):
        noOfSwaps = 0
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] , a[j]
                noOfSwaps += 1
                numSwaps += 1
         
        if noOfSwaps == 0:
            break;
            
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")
    
