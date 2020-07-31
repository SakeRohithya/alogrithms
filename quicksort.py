import random
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    print('1',A[p:r],A[i+1])
    return i+1

def quicksort(A,p,r):
    if p<r:
        #q=randompartition(A,p,r)
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def randompartition(A,p,r):
    i=random.randint(p,r)
    A[i],A[r]=A[r],A[i]
    return partition(A,p,r)
    


    
A=[2,8,7,1,3,5,6,4]
quicksort(A,0,len(A)-1)
print('After quicksort:',A)

