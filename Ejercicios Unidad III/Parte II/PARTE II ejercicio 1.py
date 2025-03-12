import numpy as np 
import matplotlib.pyplot as plt  

class matriz:  
    def __init__(self, n): 
        n1 = n
        self.iteraciones = 10  
        m = np.random.uniform(1, 10, size=(n1, n1)) 
        self.matriz = (m + m.T) / 2
        self.vector = np.random.rand(n)
        self.autovalor_mas_pequeño = 0
        self.autovalores_metodo_potencia = []  
        self.autovalores_metodo_potencia_inverso = []
        self.condicion()  
        self.metodo_potencia()  
        self.metodo_potencia_inverso()  

    def condicion(self):  # Verifica condición
        condicionM = np.linalg.cond(self.matriz)
        print(condicionM)
        if condicionM > 4:  
            print(f"El numero de condición de la matriz C es de : {condicionM}")
            print("Posibles problemas de estabilidad")

    def metodo_potencia(self):  # Método de potencia
        copiaM = self.matriz.copy()
        copiaV = self.vector.copy()
        for i in range(self.iteraciones):
            v = np.dot(copiaM, copiaV) / np.linalg.norm(copiaV)
            self.autovalores_metodo_potencia.append(np.linalg.norm(v))
            autovalore = np.linalg.norm(v)
            copiaV = v
        self.autovalore = autovalore
        print(f"El riesgo principal del portafolios es de : {autovalore}")

    def metodo_potencia_inverso(self):  # Método inverso
        copiaM = self.matriz.copy()
        copiaV = self.vector.copy()
        copiaV = copiaV / np.linalg.norm(copiaV)
        for i in range(self.iteraciones):
            v = np.linalg.solve(copiaM, copiaV)
            v = v / np.linalg.norm(v)
            autovalor = np.dot(v.T, np.linalg.solve(copiaM, v))
            self.autovalores_metodo_potencia_inverso.append(1 / autovalor)
            copiaV = v
        self.autovalor_mas_pequeño = 1 / autovalor
        print(f"La combinación de activos con menos riesgo es de  : {self.autovalor_mas_pequeño}")

    def graficar(self):  # Método para graficar
        plt.plot(self.autovalores_metodo_potencia, color='r', linestyle='--', label='metodo de potencia')
        plt.plot(self.autovalores_metodo_potencia_inverso, color='b', linestyle='-', label='metodo potencia inverso')
        plt.legend()
        plt.grid(True)
        plt.show()

m = matriz(3)  
m.graficar() 
