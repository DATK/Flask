from random import randint
import time

def add_to_array(n,array=[]):
    array.append(n)
    return array


def generate_array(n, a=0, b=10, Repetition_array=False):
    rep = Repetition_array
    array = []
    i1 = 0
    if rep == False:
        for i in range(n):
            array.append(randint(a, b))
    else:
        if (b-a) > n and b > a:
            while i1 <= n:
                tmp = randint(a, b)
                if tmp not in array:
                    array.append(tmp)
                    i1 += 1
                else:
                    continue
        else:
            print("(b-a) must be < than n")
            exit()
    i1 = 0
    return array


def sort_pus(array):
    for i in range(len(array)):
        for j in range(i+1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def sort_long(array):
    i = 0
    j = 1
    i1=0
    j1=1
    while True:
        i=0
        j=1
        i1=0
        j1=1
        while j <= len(array)-1:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                i += 1
                j += 1
                i1+=1
                j1+=1
                continue
            else:
                i += 1
                j += 1
                continue
        if j1==1:
            break
    return array


def such_elem(elem, array):
    for i in range(len(array)):
        if elem == array[i]:
            return i
    return 404

"""
print("-----------------------------------")
xs = time.time()
r = generate_array(300, -50000, 200000, False)
print("--- %s seconds ---" % (time.time() - xs))
r1=r.copy()
r2=r.copy()

s = time.time()
sort_pus(r)
print("--- %s seconds ---" % (time.time() - s))

sas = time.time()
sort_long(r1)
print("--- %s seconds ---" % (time.time() - sas))

s1 = time.time()
such_elem(elem=3, array=r)
print("--- %s seconds ---" % (time.time() - s1))


s11 = time.time()
r2.sort(reverse=True)
print("--- %s seconds ---" % (time.time() - s11))
print("-----------------------------------")

#print(r2)
#print(r)
#print(r1)
if r==r1:
    print("r1=r")
else:
    print("Somthing not that")

"""