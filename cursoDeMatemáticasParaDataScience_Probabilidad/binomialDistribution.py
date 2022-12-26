import numpy as np
from numpy.random import binomial
from scipy.stats import binom
from math import factorial
import matplotlib.pyplot as plt

def plot_hist(num_trials):
  values = [0,1,2,3] #Possible results
  arr = []
  for _ in range(num_trials):  #We simulate a num_trials of experiments 
    arr.append(binomial(3, 0.5)) #Using binomal from np.random module to get diffrent samples from binomial distribution 
                                 #It simulates fliping a balanced (p=0.5) coin 3 times (n=3) 
  simDist= np.unique(arr, return_counts=True)[1]/len(arr) #Getting the percentage of each unique possible outcome
                                                          #from the simulation
  theoDist= [binom(3, 0.5).pmf(k) for k in values] #Getting the percentage of each unique possible result applying
                                                   #the binomial distribution
  plt.bar(values, simDist, label = 'teoría', color = 'red')
  plt.bar(values, theoDist, label = 'simulación', alpha = 0.5, color = 'blue')
  plt.title('simulación con {} experimentos'.format(num_trials))
  plt.show()


def main():
    plot_hist(20)
    plot_hist(200)
    plot_hist(20000)



if __name__=="__main__":
    main()

