import urllib2;import json

def loop(d):
    for i in range(0, d):
        aux =float(d / 1024)
    return aux

def fullQuantumRandomArray(dim):
    d = str(dim)
    if d < 1024:
        url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
        url2 = '&type=uint16'
        url = url1 + d + url2
        response = urllib2.urlopen(url)
        data = json.load(response)
        num = data.get("data", "none")
        return num
    else:
        for (d/1024)

        import numpy as np
        Array = np.zeros(d)
        for i in range(0,d):
            aux2=
            aux=i/1024
            if aux is format(int):
                url = 'https://qrng.anu.edu.au/API/jsonI.php?length=1024&type=uint16'
                a = urllib2.urlopen(url)
                data = json.load(a)
                num = data.get("data")
            Array[i]=
            [i]=numint(num[i])
        for i in range(0,d,1024):
            url = 'https://qrng.anu.edu.au/API/jsonI.php?length=1024&type=uint16'
            a = urllib2.urlopen(url)
            data = json.load(a)
            num = data.get("data")

            if aux is format(int):
                url = 'https://qrng.anu.edu.au/API/jsonI.php?length=1024&type=uint16'
                a = urllib2.urlopen(url)
                data = json.load(a)
                num = data.get("data")
        for i in range(0,d):
            Array[i]=int(num[i])
            aux = i / 1024
            return Array
print fullQuantumRandomArray(1026)
while aux is not format(int):
    for i in range(0, d):
        Array[i] = int(num[i])
        aux = i / 1024
        return Array

