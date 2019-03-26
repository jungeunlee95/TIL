import sys
sys.stdin = open("input","r")

def find(n,cnt,length,nums):
    result=[]
    for i in range(length):
        for j in range(10):
            if int(nums[i][-1])>j:
                result.append(nums[i]+str(j))
                if cnt==n:
                    return nums[i]+str(j)
                cnt+=1
            else:
                break
    return find(n,cnt,len(result),result)


n= int(input())
nums=['0','1','2','3','4','5','6','7','8','9']
if n<10: print(n)
elif n>1022: print(-1)
else:
    print(find(n,10,10,nums))