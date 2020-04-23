x = [1, 2, 3, 4]
y = [6, 4, 3, 2]
z = ['a', 'b', 'c', 'd']

for a,b,c in zip(x,y,z):
    print(a,b,c)

print(zip(x,y,z))
for i in zip (x,y,z):
    print(i)

print(list(zip(x,y,z)))
print(dict(zip(x,z)))
print(dict(zip(x,y)))
a= dict(zip(x,y))
print(a)
print(a[3])


[print(a,b,c) for a,b,c in zip(x,y,z)]
print(x)

for x,y,z in zip (x,y,z):
    print(x,y,z)
print(x)