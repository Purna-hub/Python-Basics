tup1 = ('abc',101,102.4,"sultana")

tup2=(100,'sita',101.4,27.3)

#printing tuple values
print(tup1)

#printing datatype of tup1
print(type(tup1))

#demo of power operator
print(tup1*3)

#demo of slice operator
print(tup1[0:2])

#before modification of contenct in tup1
print(tup2)

tup2[0] = "xyz"
#after modification of contenct in tup1
print(tup2)