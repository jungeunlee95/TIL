"""
>문제
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는
 프로그램을 작성하시오. 

> 입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

> 출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""
def check(i):
    if(i < 100): return i
    else:
        count = 99
        for num in range(100, i+1):
            count+=hansu(num)
        if(i==1000) : count -=1
        return count


def hansu(num):
    l,m,r=str(num)[0],str(num)[1],str(num)[2]
    l,m,r=int(l),int(m),int(r)
    if l-m==m-r:
        return 1
    else:
        return 0

n=int(input())
print(check(n))