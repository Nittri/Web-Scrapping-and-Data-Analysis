'''a=-1
def sum(n):
    global a
    if(a==len(n)-1):
        return 0
    a+=1
    return(int(n[a])+sum(n))
num=input("Enter the number:")
print(sum(num))
'''

'''
10    1010
0 1 0 1
'''
'''
def bini(n):
    if(n==0):
        return ''
    return((str(bini(n//2))+str(n%2)))

n=int(input("Enter the decimal: "))
print(bini(n))
'''

'''
def is_power_of_4(n):
    if(n==4):
        return "T"
    elif(n//4==n/4):
        return(is_power_of_4(n/4))
    else:
        return 'F'

n=int(input("Enter the number: "))
print(is_power_of_4(n))
'''


L=[1,2,3]
L2=[]
a=0
def get(a,i):
    if(a>n):
        return ''
    return (str(a)+'.'+str(get(a+L[i],i)))
n=int(input())
for i in range (len(L)):
    L2.append(get(a,i).split('.')[:-1])
    a=0
print(L2)
a=0
count=0
L=[0,0,0]
def count_ways_to_reach(n,L):
    global a,count
    print(L)
    print(int(L2[0][L[0]])+int(L2[1][L[1]])+int(L2[2][L[2]]))
    if((int(L2[0][L[0]])+int(L2[1][L[1]])+int(L2[2][L[2]]))==n):
        count+=1
    if(L[2]==len(L2[2])-1):
        print("Hi")
        return None
    L[a]+=1
    if(L[a]== len(L2[a])-1):
        L[a]=0
        a+=1
    count_ways_to_reach(n,L)
count_ways_to_reach(n,L)
print(count)
