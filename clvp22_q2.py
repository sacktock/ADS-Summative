
###solution in python 3.7.1###

##43 lines of code##

k_numbers = {}

def count_ephemeral(n1,n2,k):
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

    if n1 < 1:
        return

    count = 0 #initialize counter to 0
    
    for ni in range(n1,n2):
        if isK_ephemeral(ni,k): #increment counter if ni is k-ephemeral
            count += 1
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
