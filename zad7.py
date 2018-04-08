# Python 3.6
import sys


def section():
    elements0, elements1 = [], []
    
    num_param0 = int(input("Podaj liczbę elementów pierwszego zbioru: "))
    for i in range(num_param0):
        elements0.append(float(input("Podaj " + str(i) + ". element: ")))
    
    num_param1 = int(input("Podaj liczbę elementów drugiego zbioru: "))
    for j in range(num_param1):
        elements1.append(float(input("Podaj " + str(j) + ". element: ")))
        
    if (num_param0 != num_param1):
        print ("Zbiory są nieporównywalne!")
        sys.exit()
    else:
        for k in range(num_param0):
            if (elements0[k] <= elements1[k]):
                results.append(elements0[k])
            else:
                results.append(elements1[k])
    
    print ("\nPrzekrój podanych 2 zbiorów: ")
    for m in range(num_param0):    
        print ("Wynik obliczeń dla " + str(m) + ". elementu: " + str(results[m]))
        
def sum():
    elements0, elements1 = [], []
    
    num_param0 = int(input("Podaj liczbę elementów pierwszego zbioru: "))  
    for i in range(num_param0):
        elements0.append(float(input("Podaj " + str(i) + ". element: ")))
    
    num_param1 = int(input("Podaj liczbę elementów drugiego zbioru: "))
    for j in range(num_param1):
        elements1.append(float(input("Podaj " + str(j) + ". element: ")))
        
    if (num_param0 != num_param1):
        print ("Zbiory są nieporównywalne!")
        sys.exit()
    else:
        for k in range(num_param0):
            if (elements0[k] <= elements1[k]):
                results.append(elements1[k])
            else:
                results.append(elements0[k])
    
    print ("\nSuma podanych 2 zbiorów: ")
    for m in range(num_param0):    
        print ("Wynik obliczeń dla " + str(m) + ". elementu: " + str(results[m]))
        
def completion():
    elements = []
    num_param = int(input("Podaj liczbę elementów zbioru: "))
    
    for i in range(num_param):
        elements.append(float(input("Podaj " + str(i) + ". element: ")))
        
    for j in range(num_param):
        results.append(1 - elements[j])
      
    print ("\nDopełnienie podanego zbioru: ")    
    for k in range(num_param): 
        print ("Wynik obliczeń dla " + str(k) + ". elementu: " + str(results[k]))    
        
def begin():
    a = float(input("Podaj parametr 'a': "))
    b = float(input("Podaj parametr 'b': "))
    c = float(input("Podaj parametr 'c': "))

    num_param = int(input("Podaj liczbę elementów: "))
    elements = []

    for i in range(num_param):
        elements.append(float(input("Podaj " + str(i) + ". element: ")))

    for j in range(num_param):
        if (a == b and b != c):
            if (elements[j] <= a):
                results.append(1)
            elif (elements[j] > a and elements[j] < c):
                # Xa = a, Ya = 1, Xc = c, Yc = 0
                results.append((a - elements[j])/(c - a) + 1)
            else:
                results.append(0)
        elif (b == c and a != b):
            if (elements[j] >= b):
                results.append(1)
            elif (elements[j] > a and elements[j] < b):
                # Xa = a, Ya = 0, Xb = b, Yb = 1
                results.append((elements[j] - a)/(b - a))
            else:
                results.append(0)
        else:
            if (elements[j] == b):
                results.append(1)
            elif (elements[j] <= a):
                results.append(0)
            elif (elements[j] > a and elements[j] < b):
                # Xa = a, Ya = 0, Xb = b, Yb = 1
                results.append((elements[j] - a)/(b - a))
            elif (elements[j] > b and elements[j] < c):
                # Xa = b, Ya = 1, Xb = c, Yb = 0
                results.append((b - elements[j])/(c - b) + 1)
            else:
                results.append(0)
                
    for k in range(num_param):
        print ("\nElement " + str(k) + ". równy " + str(elements[k]))
        print ("Wynik obliczeń dla tego elementu: " + str(results[k]))
        

results = []
print ("a) Obliczanie singletonów zbioru")
print ("b) Obliczanie przekroju 2 zbiorów")
print ("c) Obliczanie sumy 2 zbiorów")
print ("d) Obliczanie dopełnienia zbioru")
option = input("Wybierz jedną z opcji: ")

if (option == 'a'):
    begin()
elif (option == 'b'):
    section()
elif (option == 'c'):
    sum()
elif (option == 'd'):
    completion()
else:
    print ("Wybrałeś nieprawidłową opcję!")
    sys.exit()        
    