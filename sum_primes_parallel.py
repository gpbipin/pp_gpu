#!/usr/bin/python
# File: sum_primes_parallel.py
# Original Author: VItalii Vanovschi
# Forked by: Bipin
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com

import math, sys, time
import pp

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

# tuple of all parallel python servers to connect with
ppservers = ()
#ppservers = ("10.0.0.1",)

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)
##print job_server



print("Starting pp with", job_server.get_ncpus(), "workers")

# Submit a job of calulating sum_primes(100) for execution.
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before sum_primes execution
# Execution starts as soon as one of the workers will become available
job1 = job_server.submit(sum_primes, (100,), (isprime,), ("math",))

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will wait here until result is available
result = job1()

print("Sum of primes below 100 is", result)

start_time = time.time()

# The following submits 8 jobs and then retrieves the results
inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
jobs = [(input, job_server.submit(sum_primes,(input,), (isprime,), ("math",))) for input in inputs]
for input, job in jobs:
    print("Sum of primes below", input, "is", job())

print("Time elapsed: ", time.time() - start_time, "s")
job_server.print_stats()

# Parallel Python Software: http://www.parallelpython.com


#=================
"""
202205012232: AMD Ryzen 9 3900 12 cores, 24 threads with 16GB RAM

Usage: python sum_primes.py [ncpus]
    [ncpus] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system

('Starting pp with', 24, 'workers')
('Sum of primes below 100 is', 3889)
('Sum of primes below', 100000, 'is', 4545553462L)
('Sum of primes below', 100100, 'is', 4554958172L)
('Sum of primes below', 100200, 'is', 4564071743L)
('Sum of primes below', 100300, 'is', 4573294631L)
('Sum of primes below', 100400, 'is', 4582426348L)
('Sum of primes below', 100500, 'is', 4591667716L)
('Sum of primes below', 100600, 'is', 4600717312L)
('Sum of primes below', 100700, 'is', 4609977036L)
('Sum of primes below', 100000, 'is', 4545553462L)
('Sum of primes below', 100100, 'is', 4554958172L)
('Sum of primes below', 100200, 'is', 4564071743L)
('Sum of primes below', 100300, 'is', 4573294631L)
('Sum of primes below', 100400, 'is', 4582426348L)
('Sum of primes below', 100500, 'is', 4591667716L)
('Sum of primes below', 100600, 'is', 4600717312L)
('Sum of primes below', 100700, 'is', 4609977036L)
('Sum of primes below', 100000, 'is', 4545553462L)
('Sum of primes below', 100100, 'is', 4554958172L)
('Sum of primes below', 100200, 'is', 4564071743L)
('Sum of primes below', 100300, 'is', 4573294631L)
('Sum of primes below', 100400, 'is', 4582426348L)
('Sum of primes below', 100500, 'is', 4591667716L)
('Sum of primes below', 100600, 'is', 4600717312L)
('Sum of primes below', 100700, 'is', 4609977036L)
('Time elapsed: ', 84.8659999370575, 's')
Job execution statistics:
 job count | % of all jobs | job time sum | time per job | job server
        25 |        100.00 |     1993.9170 |    79.756680 | local
Time elapsed since server creation 84.8659999371
0 active tasks, 24 cores
"""
