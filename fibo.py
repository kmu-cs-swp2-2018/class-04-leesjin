import time

def fibo(n):
    if n <=1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    a = [0, 1]

    for i in range(2, n + 1):
        a.append(a[i - 1] + a[i - 2])
    return a[-1]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() -ts
    print("InterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() -ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
