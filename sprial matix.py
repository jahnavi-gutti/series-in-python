#print sprial matrix
def spiral(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)
        arr=list(zip(*arr))[::-1]
    return ans
arr=[]
r,c=[int(v) for v in input().split()]
for i in range(r):
    cur=[int(v) for v in input().split()]
    arr.append(cur)
print(spiral(arr))
"""
3 3
1 2 3
4 5 6
7 8 9
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""
