import math
import copy

'''
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2) O(1)
    a = lst.pop()  O(1)
    b = lst.pop(0) O(N)
    lst.insert(0, a) O(N)
    lst.append(b) O(1)
A. slow1 switches the first and last values of the list.
B. O(N)
C. 
def speedGonzalez1(lst):
    assert(len(lst) >= 2) O(1)
	lst[0], lst[len(lst)-1] = lst[len(lst)-1], lst[0] O(1)
D. O(1)
'''

'''
def slow2(lst): # N is the length of the list lst
    counter = 0 O(1)
    for i in range(len(lst)): O(N)
        if lst[i] not in lst[:i]: O(N)
            counter += 1 O(N)
    return counter
A. Counts how many values don't repeat.
B. O(N^2)
C. 
def speedyGonzalez2(lst):
	return len(set(lst))
D. O(N)

import string
def slow3(s): # N is the length of the string s
    maxLetter = "" O(1)
    maxCount = 0 O(1)
    for c in s: O(N)
        for letter in string.ascii_lowercase: O(26)
            if c == letter: O(1)
                if s.count(c) > maxCount or s.count(c) == maxCount and c < maxLetter: O(N)
                    maxCount = s.count(c) O(N)
                    maxLetter = c O(1)
    return maxLetter

A. Returns the most frequent lower case letter.
B. O(N^2)
C.
def speedyGonzalez3(s):
    d = dict() #O(1)
    result = set() #O(1)
    highest = 0 #O(1)
    lower = "" #O(1)
    for i in s: #O(n)
        if (ord("a") <= ord(i) <= ord("z")): #O(1)
            lower += i #O(1)
    for i in lower: #O(n)
        if i in d: #O(1)
            d[i] += 1 #O(1)
        else: #O(1)
            d[i] = 1 #O(1)
    for key in d: #O(n)
        if d[key] > highest: #O(1)
            result = set(key) #O(1)
            highest = d[key] #O(1)
        elif d[key] == highest: #O(1)
            result.add(key) #O(1)
    if len(result) == 1: #O(1)
        return result.pop() #O(1)
    elif len(result) == 0: #O(1)
        return None #O(1)
    return result #O(1)
D. O(N)
'''

def invertDictionary(d):
	inverted = {} #dictionary to be inverted
	k = d.keys() #gets all keys of dictionary
	v = d.values() #gets all values of dictionary

	for key, value in d.items(): #gets key and value
		if value not in inverted.keys(): #if there isn't already a key with the same value
			inverted[(value)] = set() #creates a new set
		inverted[value].add(key) #adds key to the set in the value
	return inverted


def largestSumOfPairs(a):
	if len(a) <= 1: #if list is less than or equal to 1
		return None
	max1 = max(a) #gets first max
	a.remove(max1) #removes max
	max2 = max(a) #gets second max
	return max1 + max2 #returns sum of two highest nums in list

def testLargestSumOfPairs():
	assert(largestSumOfPairs([1,2,3,4,5])==9)
	assert(largestSumOfPairs([]) == None)
	assert(largestSumOfPairs([2,2])==4)
	assert(largestSumOfPairs([1])==None)
	
def testInvertDictionary():
	assert(invertDictionary({1:2})=={2: {1}})
	assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == {2:set([1]), 3:set([2,5]), 4:set([3])})
	assert(invertDictionary({"br":2, 2:"br"}) == {2: {'br'}, 'br': {2}})
	assert(invertDictionary({1:1}) == {1: {1}})

def test():
	print("Testing invertDictionary...")
	testInvertDictionary()
	print("Passed!")
	print("Testing largestSumOfPairs...")
	testLargestSumOfPairs()
	print("Passed!")

test()

