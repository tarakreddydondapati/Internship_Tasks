n=int(input())
arr=set(map(int,input().split()))
m=int(input())
arr2=set(map(int,input().split()))
l=arr.difference(arr2)
print(len(l))

#https://www.hackerrank.com/challenges/py-set-difference-operation/problem