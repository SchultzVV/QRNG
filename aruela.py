import random
a=[random.random() for i in range(0,10000)]
print (sum(a))
print(a)
b=[sum(a)for i in range(0,10000)]
c=[a[i]/b[i] for i in range(0,10000)]
print(sum(c))
print(b)
print(c)
