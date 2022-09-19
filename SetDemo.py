
#declaring a set with some variable

set1={1,'sudha',101.3,"kumar",1}

#declaring set with set() fuction
set2 = set() #empty set
set2.add(1)	#adding element to empty set
set2.add(10.6)

#displaying set elements
print(set1)
print(set2)

set1.add('hope')
print("before update:")
print(set1)

set1.update([2,'raja'])
print("after update:")
print(set1)