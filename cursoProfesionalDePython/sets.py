mySet1 = {3, 4, 5}
mySet2 = {5, 6, 7}

#With operators

mySet3 = mySet1 | mySet2 #union
print(mySet3)

mySet3 = mySet1 & mySet2 #intersection
print(mySet3)

mySet3 = mySet1 - mySet2 #difference ex.1
print(mySet3)

mySet3 = mySet2 - mySet1 #difference ex.2
print(mySet3)

mySet3 = mySet1 ^ mySet2 #symmetric difference
print(mySet3)

#With methods
mySet3 = mySet1.union(mySet2) #union
print(mySet3)

mySet3 = mySet1.intersection(mySet2) #intersection
print(mySet3)

mySet3 = mySet1.difference(mySet2) #difference ex.1
print(mySet3)

mySet3 = mySet2.difference(mySet1) #difference ex.2
print(mySet3)

mySet3 = mySet1.symmetric_difference(mySet2) #symmetric difference
print(mySet3)