x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))

y = x
print(y is x) #True
print (y is [1, 2, 3]) #False

x.append(4)
print(x)
print(y)

print(type(id(x)))