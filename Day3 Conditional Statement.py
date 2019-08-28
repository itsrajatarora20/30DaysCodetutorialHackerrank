#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N>20:
        if N%2==0:
            print("Not Weird")
        else:print("Weird")
    elif N<=20:
        if N<=5:
            if N%2==0:
                print("Not Weird")
            else:
                print("Weird")
        if N>=6:
            if N%2==0:
                print("Weird")
            else:
                print("Not Weird")
