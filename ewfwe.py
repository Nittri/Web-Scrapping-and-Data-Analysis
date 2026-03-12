'''def loop(n):
    for i in d[n]:
        yield i
'''
'''     
d={}
D={}
def find(nums,target):
    global d
    for i in nums:
        if(target>i):
            d[i]=range(1,(target//i)+1)
        else:
            d[i]=[0]
n=0
def two(nums,target):
    global n
    if n==len(nums):
        return(0)
    for i in d[nums[n]]:
          D
          n+=1
          











    
L2=input().split(' ')
L=[]
for i in L2:
    L.append(int(i))
num=int(input())
find(L,num)
print(d,L)
'''

def find_combinations(nums, target):
    def inner(remaining, combination, start):
        if remaining == 0:  
            results.append(list(combination))
            return
        for i in range(start, len(nums)):
            if nums[i] > remaining:
                continue
            combination.append(nums[i])
            inner(remaining - nums[i], combination, i)
            combination.pop()

    nums.sort() 
    results = []
    inner(target, [], 0)
    return results


L2=input().split(' ')
L=[]
for i in L2:
    L.append(int(i))
num=int(input())
print(find_combinations(L, num))
