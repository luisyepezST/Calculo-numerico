import numpy as np  # Operaciones numéricas
import matplotlib.pyplot as plt  # Graficar

class matriz:  # Clase para matriz
    def __init__(self):
        n = 3
        self.matriz = np.random.uniform(-10, 10, size=(n, n)) 
        self.vector = np.random.rand(n) 

class metodo_potencia:  # Clase para el método de potencia
    def __init__(self, iteraciones):
        self.iteraciones = iteraciones  
        self.m = matriz() 
        self.autovalores = []  
        self.procesar() 

    def procesar(self):  # Método para calcular autovalores
        for i in range(self.iteraciones):
            v = np.dot(self.m.matriz, self.m.vector) / np.linalg.norm(self.m.vector)  
            self.autovalores.append(np.linalg.norm(v))  
            autovalore = np.linalg.norm(v)  
            self.m.vector = v  
        self.autovalore = autovalore  

class graficar:  # Clase para graficar resultados
    def __init__(self):
        self.metP = metodo_potencia(50)  
        self.gf()  

    def gf(self):  # Método de graficar
        plt.axhline(y=self.metP.autovalore, color='r', linestyle='--', label='Autovalor Dominante')  
        plt.plot(self.metP.autovalores, label='Auto vector') 
        plt.legend() 
        plt.grid(True)  
        plt.show()  

graficar()  
