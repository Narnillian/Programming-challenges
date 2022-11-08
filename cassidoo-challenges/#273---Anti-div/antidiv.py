#!/usr/bin/python
# reading https://oeis.org/A066272/a066272a.html begun 2022-11-06 (sunday)
# code begun 2022-11-07

from sys import flags as callflags
from sys import argv

#def isAD(k,n):
#    return n%k==k/2 if k%2==0 else n%k==(k-1)/2 or n%k==(k+1)/2

def antidivisor(n):
    result = []
    for k in range(2,n):
        if n%k==k/2 if k%2==0 else n%k==(k-1)/2 or n%k==(k+1)/2: result.append(k)
    print(result)

# i learned something new!
if callflags.inspect == 0:
    if len(argv)>1: antidivisor(int(argv[1]))
    else: print(
        """Please include a number as another argument, or run this script in inspect mode.
For example:
    python antidiv.py 15
    python -i antidiv.py""")
