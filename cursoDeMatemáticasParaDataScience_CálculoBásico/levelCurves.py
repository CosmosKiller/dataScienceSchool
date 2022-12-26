from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

def triDimGraph(x, y):
    x, y = np.meshgrid(x,y)

    z = np.sin(x) + 2*np.sin(y) 

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, y, z, cmap=cm.cool,linewidth=0, antialiased=False)
    fig.colorbar(surf)

    plt.show()

    return z


def lvlCurves(x, y, z, res):
    fig2,ax2 = plt.subplots()
    level_map = np.linspace(np.min(z), np.max(z),res) 
    cp = ax2.contour(x, x, z, levels=level_map,cmap=cm.cool)
    fig2.colorbar(cp)
    ax2.set_title('Curvas de nivel')

    plt.show()


def main():
    res = 100 

    x = np.linspace(-4, 4, res)
    y = np.linspace(-4, 4, res)

    z = triDimGraph(x,y)

    lvlCurves(x, y, z, res)



if __name__=='__main__':
    main()