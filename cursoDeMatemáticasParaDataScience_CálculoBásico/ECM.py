import numpy as np
import matplotlib.pyplot as plt

def estimatedB0B1(x, y):
    n = np.size(x)
    # Obtenemos los promedios de x e y
    m_x, m_y = np.mean(x), np.mean(y)

    # Sumatoria de xy y sumatoria de xx
    sumXY = np.sum((x-m_x)*(y-m_y))
    sumXX = np.sum((x-m_x)**2)

    # Coeficientes de regresión
    b1 = sumXY/sumXX

    b0 = m_y - b1 * m_x

    return b0,b1


def f(x, b):
    return b[0] + b[1]*x
  

def plotReg(x, y, b):
    plt.scatter(x, y, color = "g", marker = "o", s=30)

    yPredictions = f(x, b)
    plt.plot(x, yPredictions, color = "b")

    #etiquetado
    plt.xlabel("x - Independiente")
    plt.ylabel("y - Dependiente")

    plt.show()


def main():
    x = np.array([0,20,30,40,50,60])
    y = np.array([100,150,200,180,250,230])

    b = estimatedB0B1(x, y)

    ECM = 0
    yHat = f(x, b)
    for n in range(np.size(y)):
        ECM = ECM + (y[n]-yHat[n])**2
    ECM = ECM/(np.size(y))

    print("Los valores de b0 = {}, b1 = {}".format(b[0],b[1]))
    print("El ECM es: ", str(ECM))

    plotReg(x, y, b)



if __name__ == "__main__":
    main()