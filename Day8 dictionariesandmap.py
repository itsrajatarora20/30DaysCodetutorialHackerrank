#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    y=arr[-1::-1]
    for x in y:
        print(x,end=" ")
