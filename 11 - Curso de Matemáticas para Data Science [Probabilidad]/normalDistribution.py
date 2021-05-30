import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    #In order to import pandas you must install the dependencies via pip.
    #You may also need to install xlrd to use the read_excel fuction from pandas
    df = pd.read_excel('/home/cosmoskiller/Escritorio/Dropbox/Platzi/Escuela de Data Science/11 - Curso de Matemáticas para Data Science [Probabilidad]/s057.xls')
    arr = df['Normally Distributed Housefly Wing Lengths'].values[3:]
    values, dfDist = np.unique(arr, return_counts=True) #Getting the unique values and the count of each unique value
    dfDist = dfDist/len(arr) #Getting the percentage of each unique possible values

    mu = arr.mean()
    sigma = arr.std()
    theoDist = norm(mu, sigma)
    x = np.arange(30,60,0.1) #Building an arrange that englobes all the possible values in the df
    y = [theoDist.pdf(value) for value in x] #Applying the normal distribution to all x values in order to get y values
                                             #that complies the Gaussian function
    
    fig, ax = plt.subplots()
    ax.bar(values, dfDist)
    ax.plot(x, y)

    plt.show()



if __name__=='__main__':
    main()