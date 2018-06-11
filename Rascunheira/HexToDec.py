def decD(digit):
    digits = ['0','1','2','3','4','5','6','7','8','9','10','a','b','c','d','e','f']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x
def HextoDec(hexNum):
    dN=0
    p=0
    for digit in range(len(hexNum),0, -1):
        dN=dN+16**p*decD(hexNum[digit-1])
        p+=1
    return str(dN)
