import numpy as np  
import matplotlib.pyplot as plt 

class matriz:  
    def __init__(self, n):  
        n1 = n
        self.iteraciones = 10  
        self.cantidadI = [0, 0]  
        m = np.random.uniform(1, 10, size=(n1, n1))  
        self.matriz = (m + m.T) / 2  
        print(self.matriz)  
        self.vector = np.random.rand(n)  
        self.autovalor_mas_pequeño = 0  
        self.autovalores_metodo_potencia = []  
        self.autovalores_metodo_potencia_inverso = []  
        is_symmetric = np.allclose(self.matriz, self.matriz.T)  
        self.condicion() 
        self.metodo_potencia() 
        self.metodo_potencia_inverso()  

    def condicion(self):  # Método para calcular el número de condición de la matriz
        condicionM = np.linalg.cond(self.matriz) 
        print(f"El número de condición de la matriz es de : {condicionM}")
        if condicionM > 4: 
            print("La matriz de rigidez está mal condicionada") 

    def metodo_potencia(self):  # Método para calcular el autovalor principal
        copiaM = self.matriz.copy()
        copiaV = self.vector.copy() 
        bandera = 0  
        for i in range(self.iteraciones):  
            v = np.dot(copiaM, copiaV) / np.linalg.norm(copiaV)  
            self.autovalores_metodo_potencia.append(np.linalg.norm(v))  
            if i > 0 and abs(self.autovalores_metodo_potencia[i] - self.autovalores_metodo_potencia[i - 1]) < 1e-3 and bandera == 0:
                bandera = 1 
                self.cantidadI[0] = i  
            copiaV = v  
        self.autovalore = np.linalg.norm(v) 
        print(f"La dirección en la que la estructura es más rígida es de : {self.autovalore}")
        print(f"Tardó {self.cantidadI[0]} iteraciones en converger") 
    
    def metodo_potencia_inverso(self):  # Método para calcular el autovalor más pequeño
        copiaM = self.matriz.copy() 
        copiaV = self.vector.copy()  
        copiaV = copiaV / np.linalg.norm(copiaV) 
        bandera = 0
        for i in range(self.iteraciones):  
            v = np.linalg.solve(copiaM, copiaV) 
            v = v / np.linalg.norm(v)  
            autovalor = np.dot(v.T, np.linalg.solve(copiaM, v)) 
            self.autovalores_metodo_potencia_inverso.append(1 / autovalor) 
        
            if i > 0 and abs(self.autovalores_metodo_potencia_inverso[i] - self.autovalores_metodo_potencia_inverso[i - 1]) < 1e-3 and bandera == 0:
                bandera = 1  
                self.cantidadI[1] = i  
            copiaV = v 
        self.autovalor_mas_pequeño = 1 / autovalor  
        print(f"La dirección en la que la estructura es más vulnerable es de : {self.autovalor_mas_pequeño}")
        print(f"Tardó {self.cantidadI[1]} iteraciones en converger")
    
    def graficar(self):  # Método para graficar los resultados
        plt.plot(self.autovalores_metodo_potencia, color='r', linestyle='--', label='metodo de potencia')  # Grafica el método de potencia
        plt.plot(self.autovalores_metodo_potencia_inverso, color='b', linestyle='-', label='metodo potencia inverso')  # Grafica el método inverso
        plt.legend() 
        plt.grid(True) 
        plt.show()  

m = matriz(3)  
m.graficar()  
