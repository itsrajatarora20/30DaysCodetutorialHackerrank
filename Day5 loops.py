#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for p in range(1,11):
        print("%d x %d = %d"%(n,p,n*p))
