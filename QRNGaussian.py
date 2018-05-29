def QRNGGaussian(d):
    import math
    from QRNG import GetAnysizeArray;import numpy as np
    D=GetAnysizeArray(d)
    aux=np.zeros(d)
    for i in range(0,d):    # Looping para limitar o vetor entre [0,1)
        aux[i]=65535        # O teste requer valores neste intervalo...
    D=D/aux
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i])
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    return x


import matplotlib.pyplot    as plt
def plotHistogram(y,x):
    #populationAges = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 55,
    #                  44, 66, 77, 33, 22, 99, 88, 77, 66, 55, 44, 33, 11, 23, 45, 67, 89]
    x=QRNGGaussian(16)
    #ids = [x for x in range(len(populationAges))]
    # plt.bar(ids,populationAges)
    bins = [-3.5, -3,-2.5, -2, -1.5, -1, -0.5, 0, 0.5,1.0,1.5,2,2.5,3,3.5,4]
    plt.hist(y, x, histtype='bar', rwidth=0.8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def Test(d):
    from QRNG import Contador
    x=QRNGGaussian(d)
    y= Contador(0,d)
    from plots import plotScatter
    #plotScatter(y,x)
    bins = [-3.5, -3,-2.5, -2, -1.5, -1, -0.5, 0, 0.5,1.0,1.5,2,2.5,3]
    plotHistogram(y,bins)
Test(100)
