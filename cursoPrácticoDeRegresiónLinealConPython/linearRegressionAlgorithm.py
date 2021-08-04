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


def plotReg(x, y, b):
    plt.scatter(x, y, color = "g", marker = "o", s=30)

    yPredictions = b[0] + b[1]*x
    plt.plot(x, yPredictions, color = "b")

    #etiquetado
    plt.xlabel("x - Independiente")
    plt.ylabel("y - Dependiente")

    plt.show()


def main():
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,5,6,5])

    b = estimatedB0B1(x, y)
    print("Los valores de b0 = {}, b1 = {}".format(b[0],b[1]))

    plotReg(x, y, b)



if __name__ == "__main__":
    main()