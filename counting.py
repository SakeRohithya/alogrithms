def counting(A):
    ma=0
    B=[]
    C=[]
    for i in range(len(A)):
        if ma<A[i]:
            ma=A[i]
        B.append(0)
    for i in range(ma+1):
        C.append(0)
    for i in range(len(A)):
        C[A[i]]+=1
    for i in range(1,ma+1):
        C[i]+=C[i-1]
    for i in range(len(A)):
        B[C[A[i]]-1]=A[i]
        print('Final B:',B)
        C[A[i]]-=1
    return B

#A=[2,5,3,0,2,3,0,3]
A=[6,0,2,0,1,3,4,6,1,3,2]
print(counting(A))
        
            
