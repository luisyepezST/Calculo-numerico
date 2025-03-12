import numpy as np 
import matplotlib.pyplot as plt 

class matriz:  # Clase para definir una matriz y un vector
    def __init__(self):
        self.matriz = np.array([[2, 1], [1, 5]]) 
        self.vector = np.array([1, 1])  

class metodo_potencia_inverso:  # Clase para el método de la potencia inversa
    def __init__(self, iteraciones):  
        self.iteraciones = iteraciones  
        self.m = matriz()  
        self.autovalores = []  
        self.autovalor_mas_pequeño = 0 
        self.procesar()  

    def procesar(self):  # Método para calcular el autovalor más pequeño
        self.m.vector = self.m.vector / np.linalg.norm(self.m.vector) 
        for i in range(self.iteraciones): 
            v = np.linalg.solve(self.m.matriz, self.m.vector)  
            v = v / np.linalg.norm(v) 
            autovalor = np.dot(v.T, np.linalg.solve(self.m.matriz, v)) 
            self.autovalores.append(1 / autovalor)  
            self.m.vector = v 
        self.autovalor_mas_pequeño = 1 / autovalor  

class graficar:  # Clase para graficar resultados
    def __init__(self):
        self.metP = metodo_potencia_inverso(10)  
        self.gf()  

    def gf(self):  # Método para graficar
        plt.axhline(y=self.metP.autovalor_mas_pequeño, color='r', linestyle='--', label='Autovalor mas pequeño') 
        plt.plot(self.metP.autovalores, label='Autovectores')  
        plt.legend()  
        plt.grid(True)  
        plt.show()  

graficar()  