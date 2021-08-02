import matplotlib.pyplot as plt
import numpy as np

def f(x):
    # return np.cos(x)
    return np.sin(x)


def main():
    res = 1000

    x = np.linspace(-20.0,20.0, num = res)

    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.grid()
    ax.axhline(y = 0, color = 'r')
    ax.axvline(x = 0, color = 'r')

    plt.show()


if __name__ == '__main__':
    main()