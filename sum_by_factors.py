#From http://www.codewars.com/kata/54d496788776e49e6b00052f

#Description:

#Given an array of positive or negative integers

#I= [i1,..,in]

#you have to produce a sorted array P of the form

#[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

#P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java or C# and as an array of arrays in Python, Ruby or Clojure.

#Example:

#I = [12, 15] 
#result = [[2, 12], [3, 27], [5, 15]]

#[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

#Note: It can happen that a sum is 0 if some numbers are negative!

#Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

from collections import OrderedDict
def sum_for_list(lst):
    primeFactors = OrderedDict()
    for num in lst:
        isPrime = True
        if num in [-1, 0, 1]: continue
        for n in range(2, int(abs(num) / 2) + 1):
            if num % n == 0:
                isPrime = False
                if n in primeFactors:
                    primeFactors[n] += num
                else:
                    for n2 in range(2, int(n / 2) + 1):
                        if n % n2 == 0:
                            break
                    else:
                        primeFactors[n] = num
        if isPrime: primeFactors[num] = num
    return sorted([[prime, primeFactors[prime]] for prime in primeFactors], key=lambda pair: pair[0])
