# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:15:28 2017

@author: isperetz
"""
s = 'azcbobobegghakl'

longestsize = 0
longeststr = ''
currsize = 0
prevchr = ' '
currstr = ''
for onechr in s:
   print(s,onechr,prevchr,currstr,currsize,longeststr,longestsize)
   if onechr >= prevchr:
      currsize += 1
      currstr += onechr
      if currsize > longestsize:
         longestsize = currsize
         longeststr = currstr
   else:
      currsize = 1
      currstr = onechr
   prevchr = onechr
print('Longest substring in alphabetical order is:',longeststr)
