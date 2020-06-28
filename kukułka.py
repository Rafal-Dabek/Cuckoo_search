import random
import math
    
min=-10
max=10
def bubble_sort(A,funkcja,n):
	for i in range (0, len(A) - 1):
		for j in range (0, len(A) - i - 1):
			if math.fabs(funkcja(A[j],n))< math.fabs(funkcja(A[j+1],n)):
				A[j], A[j+1] = A[j+1], A[j]  
                

def funkcja(k,n):
    f=0
    for i in range(n):
         f+=k[i]*k[i]
    return f 
def funkcja2(k,n):
    f=0
    l=1
    for i in range(n):
         f+=k[i]*k[i]*l
         l+=1
    return f        
    


def kuku(funkcja,n):

    
    najlepsze=[]    
    tablica=[]   
    for i in range (0,100):
        xi=[]
        for j in range (n):
            xi.append(random.uniform(min,max))
        tablica.append(xi)
    bubble_sort(tablica,funkcja,n)  



    for i in range (0,10):
        yi=[]
        for j in range (n):
            yi.append(random.uniform(min,max))
        najlepsze.append(xi)
    bubble_sort(najlepsze,funkcja,n)  
       
    
   
    k=0
    while k<100:
        bubble_sort(tablica,funkcja,n)
        for i in range (90,100):   
            for j in range(n):
                najlepsze[i-90][j]=tablica[i][j]
    
        for i in range (100):
            if i<10:
                for j in range(n):
                    tablica[i][j]=najlepsze[i][j]
            else:
                for j in range(n):
                    tablica[i][j]=random.uniform(min,max)
        k=k+1         
    bubble_sort(najlepsze,funkcja,n)   
    print("najlepsze")
    for i in range(10):
        for j in range(n):
            print(najlepsze[i][j])
   
kuku(funkcja,5)

