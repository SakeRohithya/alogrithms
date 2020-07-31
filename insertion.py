## Insertion sort
def insertion(l1):
    for j in range(1,len(l1)):
        key = l1[j]
        i=j-1
        while i>=0 and l1[i]>key:
            l1[i+1]=l1[i]
            i=i-1
        l1[i+1]=key

l1=[2,3,1,4,7,-1,5]
a=l1[:]
print('Initial array:',l1)
insertion(l1)
print('Final array:',l1)

## Linear search:
def linear(l1,v):
    i=0
    while i<len(l1):
        if l1[i]==v:
            break
        i+=1
    if i==len(l1):
        print(Nil)
    else:
        print(i)
linear(l1,2)

## Adding in binary
from array import *
def binaryAddition(l1,l2):
    l3=[0]
    for i in range(len(l1)):
        l3.append(l1[i]+l2[i])
    i=len(l3)-1
    while i>=0:
        if l3[i]!=0 and l3[i]!=1:
            l3[i-1]= l3[i-1] + l3[i]//2
            l3[i]=l3[i]%2
    
        i=i-1
    return l3


l1 =array('b',[1,1])
l2 =array('b',[1,1])
print(binaryAddition(l1,l2))

## selection sort
def selection(l1):
    for i in range(len(l1)):
        index=i
        mi=l1[i]
        for j in range(i+1,len(l1)):
            if l1[j]<l1[index]:
                index = j
        if index!=i:
            l1[i]=l1[index]
            l1[index]=mi
    print(l1)

l1 =[5,5,8,-1,3,4]
selection(l1)
print(l1)

def binarySearch(A,v):
    low=0
    high=len(A)-1
    
    while True:
        mid=(low+high)//2
        if A[mid]==v:
            return mid
        elif mid==low:
            return None
        else:
            if A[mid]<v:
                low=mid
            elif A[mid]>v:
                high=mid
            
        
    

l1=[2,3,1,4,7,-1,5]
selection(l1)

print(binarySearch(l1,2))























    
