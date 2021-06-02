import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm


def optimal_mu(arr):
    mu = 0
    for n in range (0,len(arr)):
        mu = mu + arr[n]

    mu = mu/len(arr)
    return mu

def optimal_sigma(arr, mu):
    sigma = 0
    for n in range (0,len(arr)):
        sigma = sigma + (arr[n] - mu)**2

    sigma = np.sqrt(sigma/len(arr))
    return sigma


def main():
    #In order to import pandas you must install the dependencies via pip.
    #You may also need to install xlrd to use the read_excel function from pandas
    df = pd.read_excel('/home/cosmoskiller/Escritorio/Dropbox/Platzi/Data Science/11 - Curso de Matemáticas para Data Science [Probabilidad]/s057.xls')
    arr = df['Normally Distributed Housefly Wing Lengths'].values[3:]
    values, dfDist = np.unique(arr, return_counts=True) #Getting the unique values and the count of each unique value
    dfDist = dfDist/len(arr) #Getting the percentage of each unique possible values



    print(arr.mean(), optimal_mu(arr))
    print(arr.std(), optimal_sigma(arr,optimal_mu(arr)))


if __name__=='__main__':
    main()