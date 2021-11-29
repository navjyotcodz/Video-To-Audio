name=['chew','playing','are','total']
animal=['cat','dog','fish','goat']
age=[1,2,2,6]
z=zip(name,animal,age)
for name,animal,age in z:
    print("The %s that %s is %s"% (animal,name,age))