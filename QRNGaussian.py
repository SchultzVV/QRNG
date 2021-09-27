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

def PRNGGaussian(d):
    import math; import random as rd; import numpy as np
    D=[rd.random() for i in range (0,d)]
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i])
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    return x
#------------------------------------------------------------------------------
def plotHistogram(x):
    import matplotlib.pyplot    as plt
    #bins = [-2.5,-2.25, -2,-1.75,-1.5, -1.25, -1,-0.75, -0.5,-0.25,-0.2,-0.18,;
        #-0.16,-0.14,-0.12,-0.10,-0.05, 0,0.05,0.1,0.12,0.14,0.16,0.18,0.2,0.25, 0.5;
        #0.75,1.0,1.25,1.5,1.75,2,2.25,2.5]
    bins = [-0.32, -0.30, -0.28,-0.26, -0.24,-0.22,-0.2,-0.18,-0.16,-0.14,-0.12,-0.10,-0.05, 0,0.05,0.1,0.12,0.14,0.16,0.18,0.2,0.22, 0.24,0.26,0.28,0.30,0.32]
    plt.hist(x, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
def Ptest(d):
    import numpy as np
    x=np.random.normal(0.0,1.0,2*100)
    from plots import plotScatter
    plotHistogram(x)
Ptest(10000)

def QTest(d):
    x=QRNGGaussian(d)
    plotHistogram(x)
QTest(2040)
