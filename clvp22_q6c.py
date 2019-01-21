###solution in python 3.7.1###

def merge_sort(A): #sorts a list A in descending order
    if len(A) <= 4: #lists with length 4 or less go into the base case
        return selectionsort(A) #base case calls selection sort

    pivot = (len(A) + 1) // 2 #detemining the middle of the list (n+1)/2
    

    leftA = A[:pivot] #slicing list into 2 halves
    rightA = A[pivot:]

    leftA = merge_sort(leftA) #sorting both halves of the list
    rightA = merge_sort(rightA)

    return merge(leftA,rightA) #merging to haalves together

def merge(leftA, rightA):
    A = [] #initialise answer
    while len(leftA) > 0 and len(rightA) > 0: #loop while both lists are not empty
        if leftA[0] > rightA[0]: #append the largest element of both sublists to the answer
            A.append(leftA[0])
            leftA = leftA[1:]
        else:
            A.append(rightA[0])
            rightA = rightA[1:]
        
    if len(leftA) > 0: #append 'left-overs' to the answer
        A = A + leftA
    else:
        A = A + rightA

    return A

def selectionsort(A): #selection sort algorithm
    for i in range(0,len(A)-1):
        x = A[i] 
        p = i 
        for j in range(i+1,len(A)):
            if A[j] > x:
                x = A[j]
                p = j

        A[p] = A[i]
        A[i] = x
    return A
        
    
