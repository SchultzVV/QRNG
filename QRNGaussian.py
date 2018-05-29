def QRNGGaussian(d):
    import math
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

def Test(d):
    from QRNG import Contador
    x=QRNGGaussian(d)
    y= Contador(0,d)
    from plots import plotScatter
    plotScatter(y,x)
Test(10)
