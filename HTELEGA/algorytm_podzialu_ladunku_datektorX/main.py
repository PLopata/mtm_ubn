import numpy as np
import matplotlib.pyplot as plt
import math


if __name__ == '__main__':
    #generate gauss
    a = 1 #szerokosc jednego pixela
    mu = 0.4  # 0 < mu < 1 dla a = 1
    sigma = 0.4 # sigma zeby wartosci byly od -1 do 2
    size = 10000
    s = np.random.normal(mu, sigma, size)

    #left pixel probability
    error_func1_numerator = -mu
    error_func1_denominator = sigma * (math.sqrt(2))
    error_func1 = error_func1_numerator/error_func1_denominator
    PxI = 1 / 2 + 1 / 2 * math.erf(error_func1)

    #right pixel probability
    error_func2_numerator = mu - a
    error_func2_denominator = (sigma * (math.sqrt(2)))
    error_func2 = error_func2_numerator / error_func2_denominator
    PxIII = 1 / 2 + 1 / 2 * math.erf(error_func2)

    #center pixel probability
    PxII = 1 - (PxI + PxIII)

    print(f'Left pixel -> {PxI}\nCenter pixel -> {PxII}\nRight pixel -> {PxIII}')

    #plot gauss
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r')
    plt.show()
