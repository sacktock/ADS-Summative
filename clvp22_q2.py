import timeit

k_numbers = {}

def count_ephemeral(n1,n2,k):
    start = timeit.default_timer()

    global k_numbers
    k_numbers = {1:True} #initialize dictionary for the next calculation
    
    if n1 > n2: #if n1 is bigger than n2 then swap them
        temp = n1
        n1 = n2
        n2 = temp

    if k not in {2,3,4}: #if k is not 2,3 or 4 then return
        return

    if n2 > 10000000: #if n is bigger than 10 million then return
        return

    count = 0 #initialize counter to 0
    
    for ni in range(n1,n2):
        if isK_ephemeral(ni,k): #increment counter if ni is k-ephemeral
            count += 1

    stop = timeit.default_timer()
    print('Time: ', stop - start)
    return count

def isK_ephemeral(n,k):
    global k_numbers
    lst = [] #list stores previous k-children
    while True:
        n = k_child(n,k) #calculate next k-child
        if n in k_numbers.keys(): #if n has already been evaluated then look in dictionary
            if k_numbers[n]: #if n is k-ephemeral 
                while lst:
                    k_numbers[lst.pop()] = True #k parents are also k-ephemeral
                return True
            if not k_numbers[n]: #if n is k-eternal
                while lst:
                    k_numbers[lst.pop()] = False #k parents are also k-eternal
                return False
        
        #if n == 1: #n is k-ephemeral by definition
            #while lst:
                #k_numbers[lst.pop()] = True #k parents are also k-ephemeral
            #return True
            #this case is implicitly handled by setting k_numbers to {1:True}
            
        if n in lst: #n is k-eternal by definition
            while lst:
                k_numbers[lst.pop()] = False #k parents are also k-eternal
            return False
        lst.append(n) # add n to k-parent list
        
    

def k_child(n,k): #calculates k-child of n
    s = 0
    while n:
        s, n = s + (n % 10)**k, n // 10
    return s



#q2test.py
"""test function for question 2 of the ADS assignment, 2018-19"""

def q2test():
    """tests for the function count_ephemeral"""
    correct = True
    result = count_ephemeral(1, 10, 2)
    if result != 2:
        correct = False
        print("test failed for n1=1, n2=10, k=2; correct result is 2, result obtained was ", result)
    result = count_ephemeral(1000, 10000, 3)
    if result != 91:
        correct = False
        print("test failed for n1=1000, n2=10000, k=3; correct result is 91, result obtained was ", result)
    result = count_ephemeral(123456, 654321, 4)
    if result != 376:
        correct = False
        print("test failed for n1=123456, n2=654321, k=4; correct result is 376, result obtained was ", result)
    if correct:
        print("all tests passed")
