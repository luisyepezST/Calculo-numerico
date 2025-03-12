import numpy as np  
import random 
import matplotlib.pyplot as plt  

class matriz: 
    def __init__(self, n):  # Constructor con tamaño
        self.matriz = np.random.uniform(-10, 10, size=(n, n)) 
        self.condicion = np.linalg.cond(self.matriz)  
        self.tamaño = len(self.matriz)

class generador_matriz:  # Clase para generar matrices
    def __init__(self):
        self.lista_matriz = []  
        self.condiciones = [] 
        self.n = []  
        self.llenar()  

    def llenar(self):  # Llenar listas
        tamaño = random.randint(2, 10)
        t = 3  
        for i in range(tamaño):
            Matriz = matriz(t) 
            self.condiciones.append(Matriz.condicion) 
            self.n.append(Matriz.tamaño) 
            self.lista_matriz.append(Matriz)  
            t += 1 

class visualizar:  # Clase para visualizar
    def __init__(self):
        self.matrices = generador_matriz()  
        plt.plot(self.matrices.n, self.matrices.condiciones, marker="o")  
        plt.ylabel("condiciónes")  
        plt.xlabel("tamaños")  
        plt.show()  

grafica = visualizar()  
