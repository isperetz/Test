# Test
Play
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:26:15 2017

@author: isperetz
"""
# Paste your function here
"""
def closest_power(base,num):
    lowerExp = 0
    highExp = 99999999
    i = 0
    while True:
        exp = base ** i
        if exp <= num:
            lowerExp = i
        else:
            highExp = i
            break
        i += 1

    distLower = num - base**lowerExp
    distHigh = base ** highExp - num
    if distLower <= distHigh:
        return lowerExp
    return highExp

print(closest_power(4,1))


def deep_reverse(L):
    deep_reverse_act(L)
    for i in range(len(L)):
        deep_reverse_act(L[i])


def deep_reverse_act(L):
     for i in range(len(L) // 2):
        tmp = L[i]
        L[i] = L[-i - 1]
        L[-i - 1] = tmp

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)



def dict_interdiff(d1, d2):
    da1 = {}
    da2 = {}
    for key in d1.keys():
        val2 = d2.get(key)
        if val2 == None:
            da2[key] = d1[key]
        else:
            da1[key] = f(d1[key],d2[key])
    for key in d2.keys():
        val1 = d1.get(key)
        if val1 == None:
            da2[key] = d2[key]
    return((da1,da2))

def f(a,b):
#    return(a+b)
    return(a > b)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1, d2)) # returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})


d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2)) #returns ({1: False, 2: False, 3: False}, {})


def applyF_filterG(L, f, g):
    rE = []
    for elm in L:
        print(elm)
        if g(f(elm)) is False:
            rE.append(elm)
    for elm in rE:
        L.remove(elm)
    return(max(L))

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)

def f(i):
     return(i**2)

def g(i):
     return(i % 2 == 0 and i > 20)

L = [3,4,5,6,7,8]

print(applyF_filterG(L, f, g))
print(L)


def flatten(aList):
    wList = aList[:]
    nList = []
    subList = True
    while subList:
        nList = []
        subList = False
        for elm in wList:
            if type(elm) == list:
                for subelm in elm:
                    nList.append(subelm)
                    if type(subelm) == list:
                        subList = True
            else:
                nList.append(elm)
        wList = nList[:]
    return(nList)

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(L))


def general_poly (L):
    def apply_x(x):
        k=len(L)-1
        sumx = 0
        for i in range(0,k+1):
            #print(L[i],x,i,k,sumx)
            sumx += L[i] * (x**(k-i))
        return(sumx)
    return apply_x

fun = general_poly([1,2,3,4])
print(fun(10))

"""
def dict_invert(d):
    ret_d = {}
    for one_item in d.items():
        dict_val = ret_d.get(one_item[1],None)
        #print(dict_val,one_item)
        if dict_val == None:
            ret_d[one_item[1]] = [one_item[0]]
        else:
            #dict_val.append(one_item[0])
            #print(one_item[1],one_item[0],dict_val)
            ret_d[one_item[1]].append(one_item[0]) # = dict_val
    return(ret_d)

d = {1:10, 2:20, 3:30}
d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))
