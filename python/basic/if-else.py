#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    w = "Weird"
    nw = "Not Weird"
    if (math.fmod(n,2) == 1):
        print(w)
    elif (math.fmod(n,2) == 0 and 2<=n<=5) :
        print(nw)
    elif (math.fmod(n,2) == 0 and 6<=n<=20) :
        print(w)
    elif (math.fmod(n,2) == 0 and n>20) :
        print(nw)