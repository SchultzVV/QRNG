from QRNG import GetRandomDec
digits=1024
dim=200
file = open('Huge Numbers.txt', 'w')

ax = str([GetRandomDec(digits) for i in range(0, dim - 1)])
file.write(ax)

file.close()

vetor = open('Huge Numbers.txt', 'r')
print file.read()