# returns the union of two sets
def union(a,b):
    c = a + [x for x in b if x not in a]
    return c

# returns the intersection of two sets
def intersect(a,b):
    c = [x for x in a if x in b]
    return c

# returns the set difference of two sets
def setDiff(a,b):
    c = [x for x in a if x not in b]
    return c

# returns the symmetric difference of two sets
def symDiff(a,b):
    c = setDiff(a,b) + setDiff(b,a)
    return c

# returns the cartesian product of two sets
def cartProd(a,b):
    c = [(x,y) for x in a for y in b]
    return c

l1 = [1,2,3]
l2 = [2,3,4]
print "Union: "
print union(l1,l2)

print "Intersection: "
print intersect(l1,l2)

print "Set Difference: "
print setDiff(l1,l2)

print "Symmetric Difference: "
print symDiff(l1,l2)

print "Cartesian Product: "
print cartProd(l1,l2)
