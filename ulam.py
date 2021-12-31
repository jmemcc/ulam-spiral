import numpy as np
import matplotlib.pyplot as plt
import math as m 

# Finds all primes up to 'n' 
# Algorithm has best complexity in high-range prime searches.
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom2to(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[           k * k // 3         :: 2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3:: 2 * k] = False
            
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

# Returns cartesian coodinates given number in square spiral (https://oeis.org/A174344).
def get_all_coords(num):
    xval, yval = 0, 0
    x = np.zeros(num+1, int)
    y = np.zeros(num+1, int)
    
    if num == 1:
        return x, y
    
    for i in range(2, num+1):
        xval += m.sin(m.floor( m.sqrt(4 * i - 7)) * (m.pi/2))
        if i > 2: 
            yval += m.cos(m.floor( m.sqrt(4 * i - 7)) * (m.pi/2))
        x[i] = round(xval)
        y[i] = round(yval) * -1
 
    return x, y

def get_prime_coords(lim):
    primes = primesfrom2to(lim)
    all_coords = get_all_coords(lim)
    
    return all_coords, (all_coords[0][primes], all_coords[1][primes])
    
def plot_spiral(lim, size=10):
    all_coords, prime_coords = get_prime_coords(lim)
    
    ax = plt.subplot()
    
    # ax.plot(all_coords[0], all_coords[1], color="red", alpha=0.05)
    ax.scatter(prime_coords[0], prime_coords[1], color="black", s=size)
    
    ax.set_xticks(list())
    ax.set_yticks(list())
    
    ax.set_title("Ulam Sprial with\nLimit of {}".format(lim))
    plt.show() 

lim = input("Enter ceiling limit for prime spiral to be counted:\n> ")
plot_spiral(int(lim))

        
        