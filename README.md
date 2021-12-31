# Ulam Spiral


A simple script to generate an [Ulam spiral](https://mathworld.wolfram.com/PrimeSpiral.html) (prime spiral) using Python. 

![Ulam spiral for primes found below the integer 10,000.](/example10000.png?raw=true "Ulam spiral for primes found below the integer 10,000." )

Ulam spirals are an illustration of unexpected patterns that emerge from a set of prime numbers. 
Often the spirals are compared to those of 'random' plots to comparitively demonstrate that the prime spiral is a non-random pattern.

<img src="https://miro.medium.com/max/2000/1*jlvLZbFwMmv-nL4-1J8XbQ.png" width="527" height="260">

(Image from '[Unexpected Beauty of Primes](https://www.cantorsparadise.com/unexpected-beauty-in-primes-b347fe0511b2)' by Jesus Najera)



# Set Up
Requires installation of Python libraries `NumPy` and `Matplotlib` for plot drawing and general mathematical functions.

```bash
pip install matplotlib
pip install numpy
```

Run this script simply as a Python file with no arguments.
Script prompts user for upper limit of the prime search, before plotting the Ulam spiral.

Note: Will be changed to a more Pythonic structure (e.g. `__main__`...) soon.

# Credit
[Prime searching algorithm](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188)  `primesfrom2to(n)`

[List of x-coordinates of point moving in clockwise square spiral](https://oeis.org/A174344) *(OEIS:A174344)*

