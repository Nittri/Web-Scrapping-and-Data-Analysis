from functools import *
'''L=list(eval(input()))
def sum(a,b):
    return(a+b)
print(reduce(sum,L))
print(reduce(lambda a,b: a if a>b else b, L))

#print(reduce(sum,L))
'''
'''
c=0
s=input()
s2=input()
print(reduce(lambda c,a: c+1 if a==s2 else c, s,0))
'''
'''
c=0
s=input()
print(reduce(lambda c,a: c+1 if a==' ' else c, s,1))
'''


'''
L=list(eval(input()))
print(reduce(lambda a,b: a+b if b%2==0 else a ,L,0))
'''
'''
L1=[1,2,3]
L2=[4,5,6]
L3=[i+j for i in L1 for j in L2]
print(L3)
'''

'''
print([i**3 for i in range(2,51,2)])
'''
'''
L=[[1,2],[3,4],[5,6],[7,8]]
print([[row[i] for row in L] for i in range(2)])
'''
'''
X=[]
Y=[]
L=[[1,2],[4,5],[7,8],[10,11]]
for i in range(len(L[0])):
    for j in range (len(L)):
        X.append(L[j][i])
    Y.append(X)
    X=[]
print(Y)
'''
'''
L=['reberbhte','aewbgawgbre','wgerbre','erbserbreb','erberbethet','arwhtrjytm']
x=[L[i][j] for i in range(len(L)) for j in range(len(L[i])) if ]
print(x) 
'''

'''
L1=[1,2,3,4,5,6,7,8,9]
L2=[3,6,11,13,5,9]
print([i for i in L1 for j in L2 if i==j])
'''
#print([i for i in range(100) if i%10==0])

#print([i for i in range(0,101) if '6' in str(i)])
#print(len([i for i in 'ehviu ev iwbv i   eh bibc  ' if i == ' ']))
#print(''.join([i for i in 'oeifihv e biubv ieubvibv' if i not in 'aeiouAEIOU']))
'''
a='abcd'
b='efgh'
print({k:v for k,v in (zip(a,b))})
'''


'''a=[1,2,3,4,5]
b=list(map(lambda x: x*x*x, a))
print(list(zip(a,b)))
'''
'''
a='abcd'
b='efgh'
print(dict((zip(a,b))))
'''
'''
from math import *


c=[1.00001,2.02010,3.78182,4.32345,5.13342]
print(([round(i,c.index(i)+1) for i in c]))

'''

'''
list1=[1,2,3,4,5]
Chars=['a','b','c','d','e']

print(list(zip(list1,Chars)))
'''


'''
L=[13,64,87,35,88,90,10,100]
print([i for i in L if i>75])
'''
'''
L=[13,64,87,35,88,90,10,100]
print(list(filter(lambda x: x>75,L)))  #704640
'''

'''
List=['Orange','Mango','Apple','Apricot']
print(list(filter(lambda x: x[0] == 'A', List)))
'''
'''
def func(n,na):
    s=0
    for i in n:
        s=s+int(i)
    return s
n='1729'
print(reduce(lambda x,y: int(x)+int(y), n))'''


'''
n=[1,2,3,4,5,6]
print(reduce(lambda x,y: min(x,y),n))
'''
