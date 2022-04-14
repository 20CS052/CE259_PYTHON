# Practical AIM             :-  Find runner-up from given list.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git


n = int(input())        #taking input n
arr = map(int, input().split())
arr = list(arr)         #convert arr into list
x = max(arr)
y = -9999999
for i in range(0,n):    #for loop to find second maximum number
    if arr[i]<x and arr[i] > y:
        y = arr[i]

print(y)
