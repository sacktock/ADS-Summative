
###solutions in python 3.7.1###

def h(k): #initial hash function
    return (6*k+3)%19

def h1(k): #secondary hash function
    return 11 - (k % 11)

def hash_quadratic(d):
    table = ["-"]*19 #initialize table 
    for k in d:
        
        if k in table: #check for duplicate
            continue
        
        hashable = True #set hashable to True
        
        for c in range(0,19):
            i = (h(k) + c**2) % 19 #apply hash function and quadratic probing
            if table[i] == "-":
                break
            if c == 18: #all possibilties exhausted for this k so it is not hashable
                hashable = False 
                
        if not hashable: #other k could potentially be hashed if table is not full
            continue #continue to hash other k
        
        table[i] = k

    return table

def hash_double(d):
    table = ["-"]*19 #initialize table
    for k in d:
    
        if k in table: #check for duplicates
            continue

        hashable = True #set hashable to True
        
        for c in range(0,19):
            i = (h(k)+ c*h1(k)) % 19 #apply hash and secondary hash function
            if table[i] == "-":
                break
            if c == 18: #not hashable so table must be full
                hashable = False
                
        if not hashable: #if k is not hashable then the table is full
            return table #so return the table
        
        table[i] = k

    return table
	


