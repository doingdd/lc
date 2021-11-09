#!/usr/bin/python
import random

def rand7():
    return random.randint(1,7) 

def rand10():
    while True:
        ## a: 1--49
        a = (rand7()-1)*7+rand7()
        if a <= 40:
            return a%10 + 1

        a -= 40
        ## a: 1--63
        a = (a-1)*7+rand7()
        if a <= 60:
            return a%10 + 1

print rand10()
