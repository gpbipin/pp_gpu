#!/usr/bin/python
# File: sum_primes_serial.py
# Author: Bipin Gopinath
# Desc: This program demonstrates serial computations 
# It calculates the sum of prime numbers below a given integer in serial

import math, sys, time

def isprime(num):
# define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    return flag

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
##    print [x for x in xrange(2,n) if isprime(x) == False]
    return sum([x for x in xrange(2,n) if isprime(x)])

print( """Usage: python sum_primes.py [ncpus]
    [ncpus] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system
""")

inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)

for n in inputs:
    start_time = time.time()
    sum_1= sum_primes(n)
    print n, sum_1
    
    print("Time elapsed: ", time.time() - start_time, "s")



