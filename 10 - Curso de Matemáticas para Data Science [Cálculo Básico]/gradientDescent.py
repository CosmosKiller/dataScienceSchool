from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2+y**2


def derivate(cp, p, h):
    return (f(cp[0], cp[1]) - f(p[0], p[1])) / h


def gradient(p, h):
    grad = np.zeros(2)
    for idx, val in enumerate(p):
       cp = np.copy(p)
       cp[idx] = cp[idx] + h 

       dp = derivate(cp, p, h)
       grad[idx] = dp

    return grad


def triDimGraph(x, y, z):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, y, z, cmap=cm.cool,linewidth=0, antialiased=False)
    fig.colorbar(surf)

    plt.show()


def gradDescent(x, y, z, res, h):
    level_map = np.linspace(np.min(z), np.max(z),res) 
    plt.contourf(x, y, z, levels=level_map,cmap=cm.cool)
    plt.colorbar()
    plt.title('Descenso del gradiente', fontsize = 18)

    p = np.random.rand(2) * 8 - 4      # El  modulo .random solo entrega valores de entre 1 y 0
    plt.plot(p[0],p[1], 'o', c = 'k')  # por esa razón debemos realizar el calculo para obtener los valores 
                                       # extremos de nuestro grid (-4 y 4)
    
    lr = 0.01

    for i in range(1000):
        p = p - lr*gradient(p, h)
        if (i % 10 == 0):
            plt.plot(p[0],p[1], 'o', c = 'r')

    plt.plot(p[0],p[1], 'o', c = 'w')
    plt.suptitle("El punto minimo es: " + str(p))
    plt.show()                    


def main():
    res = 1000
    h = 0.01

    x = np.linspace(-4, 4, res)
    y = np.linspace(-4, 4, res)

    x, y = np.meshgrid(x,y)

    z = f(x,y)

    triDimGraph(x,y,z)

    gradDescent(x,y,z,res,h)

    



if __name__=='__main__':
    main()