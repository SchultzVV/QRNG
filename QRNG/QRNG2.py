import urllib.request
import numpy as np
import json
#------------------------------------------------------------------------------------
def GetAnysizeArray(dim):
   if dim <= 1024:
       little = GetRandomArray(dim)
       return little
   else:
       large = []
       m = dim
       while m > 1024:
           large.extend(GetRandomArray(1024))
           m = m - 1024
       else:
           large.extend(GetRandomArray(m))
           return large  # Gera um array de qualquer tamanho com os dados do site
#------------------------------------------------------------------------------------
def GetRandomArray(dim):
    d=str(dim)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1+d+url2
    page = urllib.request.urlopen(url, timeout=50000)
    aux = page.read()
    data = json.loads(aux.decode('utf-8'))
    num = data.get("data", "none")
    return num   # Programa que comunica com o site e recebe os dados
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
def SavingTheDat():
    A=GetAnysizeArray(10000000)
    with open("file2.dat", 'w') as f:
        for a in A:
            f.write(str(a) + '\n')

def SafeGetAnysizeArray(dim):
    with open("file2.dat", 'w') as f:
        if dim <= 1024:
            little = GetRandomArray(dim)
            for a in little:
                f.write(str(a) + '\n')
            return little
        else:
            large = []
            m = dim
            while m > 1024:
                large.extend(GetRandomArray(1024))
                m = m - 1024
                for a in large:
                    f.write(str(a) + '\n')
            else:
                large.extend(GetRandomArray(m))
                return large  # Gera um array de qualquer tamanho com os dados do site

#SafeGetAnysizeArray(10000000)
#------------------------------------------------------------------------------------
def aruela(d):
    with open("QN.txt", 'a') as f:
        while d > 1024:
            for i in range(0,d):
                A=GetRandomArray(1024)
                for a in A:
                    f.write(str(a) + '\n')
                d = d-1024
aruela(10000000)
#------------------------------------------------------------------------------------
import numpy as np
trial = np.genfromtxt("QN.txt", dtype = str)
print (len(trial))
#------------------------------------------------------------------------------------
def read():
    with open("QN.dat", 'a') as f:
        a=[]
        for i in range(0,10):
            a=f.read(str(a))
        print(a)
#read()
