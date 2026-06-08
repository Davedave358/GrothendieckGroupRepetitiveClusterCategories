from sympy import *
import numpy as np

def k_in_a(n:int,p:int) -> int:

    if n%2 == 1: # setup the variables required when n is odd, including k as found in the paper
        if p%(n+1) != 0:
            if p >= (n+3)/2:
                p = n+1 - (p%(n+1)) # uses Prop 3.4 to reduce p
            else:
                p = p%(n+1) # p is already reduced properly
        else:
            p = (n+1)/2 # deals with edge case that gives p = 0 instead of desired result
        k = (n+1)%p
        if k == 0:
            k = p

    if n%2 == 0: # set up variables when n is even
        if p%(2*(n+1)) != 0:
            if p >= n+2:
                p = 2*(n+1) - (p%(2*(n+1))) # uses Prop 3.4 to reduce p
            else:
                p = p%(2*(n+1)) # p is already reduced properly
        else:
            p = 2*(n+1) # deals with edge case of p = 0
        k = (2*(n+1))%p
        if k == 0:
            k = p
    return k

def type_a(n:int,p:int) -> str:
    k: int = k_in_a(n,p)

    eq_classes : int = gcd(int(k),int(p)) # counts equivalence classes of simple objects with respect to S_i +- S_i+p

    a = [symbols('a%d' % i) for i in range(0,int(eq_classes))] # names the equivalence classes

    simples : list = [] # list of variables with respect to all simples

    for i in range(0,n):
        simples.append(a[i%eq_classes]) # computes S_i+jp via relation S_i +- S_i+jp

    neg_sum = (-1)*sum(simples[i] for i in range(0,n)) # negative sum of all simples

    b : list = [] # list of relations

    for i in range(0,eq_classes):
        b.append(a[i] - (-1)**((n+1)*p)*a[i]) # deals with relation S_i +- S_i+p

    b.append(a[(n-p)%eq_classes] - neg_sum) # relation S_i +- S_0 for relevant i

    b = [i for i in b if i != 0] #removes trivial relations

    return f"Additive abelian group isomorphic to Z^{eq_classes} modulo the relations {b}" # returns free abelian group and list of relations

def type_d(n:int,p:int) -> str:
    p = p%(2*(n-1)) # uses result in paper that Grothendieck group is isomorphic for p = q mod 2(n-1)

    if p == 0:
        return('This is the Grothendieck Group of Dn') # Deals with obvious edge case where C_n,p = D(mod kDn)
    else:
        pass

    eq_classes : int = gcd(n-1,p) # counts equivalence classes of S_i induced by the relations S_i +- S_i+p
    if eq_classes == p and eq_classes !=1:
        eq_classes  = eq_classes -1 # deals with edge case where the injective at n is counted as its own equivalence class above

    a : list = [symbols('a%d' % i) for i in range(0,eq_classes)] # names all of the equivalence classes of simple objects (except at vertex 0 and 1)

    l = np.array(a) # converts above into an array for computation

    a_neg :list = list(l*(-1)) # negates a for computation

    for i in range(eq_classes,n-2):
        for j in range(0,(n-1)/eq_classes):
            if (j*p+i)%(n-1) != i:
                pass
            else:
                if (p + (j*p-i)%(n-1) )%2 == 1:
                    a.append(a_neg[i%eq_classes])  # finds S_i+jp in terms of S_i subject to the relation S_i + S_i+jp
                else:
                    a.append(a[i%eq_classes]) # same as above with relation S_i - S_i+jp

    x,y = symbols('x y') # names the simple objects at vertex 1 and 0

    simples = np.sum(a) + x + y # sum of all simple objects in Grothendieck group, equal to injective object at n

    neg_sim = simples * (-1) # negation for computation

    d: list = [] # list for inputting relations

    # next we deal with three cases of p > n-1, p = n-1, p < n-1, and subcases of p mod 2
    if p >= n:
        if p%2 == 0:
            d.append(a[2*(n-1)-1-p] + neg_sim), # includes the relation S_i - I_n
            d.append(x + x + sum(a[0:p-n+1])), # includes the relation S_0 - phi^p S_0
            d.append(y + y + sum(a[0:p-n+1])) # as above with S_1
        if p%2 == 1:
            d.append(a[2*(n-1)-1-p] + simples), # relation S_i + I_n
            d.append(sum(a[0:p])) # relations S_0 + phi^p S_0, and with S_1

    if p == n-1:
        if p%2 == 0:
            d.append(x + x), # relation S_0 - phi^p S_0
            d.append(y + y), # as above with S_1
        else:
            pass

    if p <= n-2:
        if p%2 == 0:
            d.append(a[n-2-p] + simples), # relation S_i - I_n
            d.append(sum(a[0:p])), # relations with S_0 and S_1
        if p%2 == 1:
            d.append(a[n-2-p] + neg_sim), # relation S_i - I_n
            d.append(x + y + sum(a[0:p])), # relations with S_0 and S_1

    if n%2 == 1 and p%(2*(n-1)) != 1 and p%(2*(n-1)) != 2*n-3:
        for i in a[0:eq_classes]:
            d.append(i+i) # edge case where we have relation S_i + S_i

    d = [i for i in d if i !=0] # removes trivial relations

    return f"Additive abelian group isomorphic to Z^{eq_classes +2} modulo the relations {d}" # returns free abelian group and list of relations

def rep_cluster_K0(x : str, n: int, p: int) -> str:
    if n >=1 and p >= 1:
        if x == 'A':
            return type_a(n,p)
        elif x == 'D':
            return type_d(n,p)
        else:
            return 'Please choose Dynkin type A or D.'
    else:
        return 'Please choose n and p to be positive integers.'