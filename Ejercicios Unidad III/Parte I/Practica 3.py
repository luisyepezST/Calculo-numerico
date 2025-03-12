import numpy as np  # Importa la librería numpy
import matplotlib.pyplot as plt  # Importa matplotlib

class matriz:  # Clase matriz
    def __init__(self): 
        self.matriz = np.array([[4, 1], [1, 3]])  
        self.vector = np.array([1, 0])  

class metodo_potencia_simetrico:  # Método de potencia simétrico
    def __init__(self, iteraciones):
        self.iteraciones = iteraciones  
        self.m = matriz()  
        self.autov = []  
        self.Autovalor = 0 
        self.procesar()  

    def procesar(self):  # Cálculo del autovalor
        for i in range(self.iteraciones):  
            v = np.dot(self.m.matriz, self.m.vector)  
            v_normalizado = v / np.linalg.norm(v)  
            numerador = np.dot(v_normalizado.T, np.dot(self.m.matriz, v_normalizado))  
            denominador = np.dot(v_normalizado.T, v_normalizado)  
            self.Autovalor = numerador / denominador  
            self.autov.append(self.Autovalor)  
            self.m.vector = v_normalizado  

class graficar:  # Clase para graficar
    def __init__(self):  
        self.metP = metodo_potencia_simetrico(100)  
        self.gf()  

    def gf(self):  # Método de graficar
        plt.axhline(y=self.metP.Autovalor, color='r', linestyle='--', label='Autovalor Dominante')  
        plt.plot(self.metP.autov, label='Auto vector')  
        plt.legend()  
        plt.grid(True)  
        plt.show()  

# Ejecuta la clase graficar
graficar()  
