d={}
'''def loop(n):
    for i in d[n]:
        yield i'''
def find(nums,target):
    global d
    for i in nums:
        if(target>i):
            Li=range(0,(target//i)+1)
            d[i]=Li
        else:
            d[i]=[0]

def find_combinations(nums, target):
    
            
        





















L2=input().split(' ')
L=[]
for i in L2:
    L.append(int(i))
num=int(input())
find(L, num)
print(d)
find_combinations(L,num)
