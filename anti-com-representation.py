"""
Aiken Kazin, 
day: 12.03.2023   
title: Decomposition of anti-commutative algebra 
on a irreducible Sn-submodules when n = 4

"""

def innerProd(s, m, k, o):
    """
    This function takes two character and return their iner product as in R^n
    
    where: s - character for some representation
           m - main representation
           k - list of size of conjugacy classes
           o - order of a symmetric group, in general ord(Sn) = n!
    """
    a = []
    for i in range(len(k)):
        a.append(k[i]*s[i])
    return int(np.inner(np.array(a), np.array(m)) / o)


def getCharacterTable():
    """
    This function returns a character table of a given symmetric group.
    (We for now will just write this table by hand)
    """
    x_1 = [1,1,1,1,1]
    x_2 = [1,-1,1,1,-1]
    x_3 = [3,1,-1,0,-1]
    x_4 = [3,-1,-1,0,1]
    x_5 = [2,0,2,-1,0]
    x = [x_1, x_2, x_3, x_4, x_5]
    return x

def getPartition():
    """
    This function returns the partitions of n.
    (For now we will write it by hand)
    """
    p_1 = [4]
    p_2 = [3,1]
    p_3 = [2,2]
    p_4 = [2,1,1]
    p_5 = [1,1,1,1]
    
    p = [p_1, p_2, p_3, p_4, p_5]
    return p

def defChar():
    """
    This function returns the defining character of Sn
    (For now we will write by hand)
    """
    
    return [15,-3,-1,0,1]

def getConjSize():
    """
    This function returns the list of sizes of a conjugacy classes of Sn
    (For now we will write it by hand)
    """
    size = [1,6,3,8,6]
    
    return size

def getRep():
    """
    This function returns the coefficients of an irreducible Sn submodules related to a given partitions
    """
    # calculate the order of a o = ord(Sn) = n!
    o = 24
    
    K = getConjSize() # list of size of conjugacy classes
    X = defChar()     # defining chararecter of Sn
    p = getPartition() # list of partitions of n
    H = getCharacterTable() # all irreducible characters (or from character table)
    
    m = []
    for i in range(len(K)):
        mi = innerProd(H[i], X, K, o)
        m.append(mi)
    return m

m = getRep()
w = ""
for i in range(5):
    w += str(m[i])+"*M"+str(tuple(p[i]))+" + "
print("P_4 = ",w[:-2])
