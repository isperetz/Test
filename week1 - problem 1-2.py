# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:49:48 2017

@author: isperetz
"""
#week 1 problem 1
#Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghaklvgg'
numvow = 0
for chr in s:
   if chr in 'aeiou':
      numvow += 1
print('Number of vowels:',numvow)


#Week 1 problem 2
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
ctr = 0
for i in range(len(s)):
   if s[i:i+3] == 'bob':
      ctr += 1
print('Number of times bob occurs is:',ctr)
