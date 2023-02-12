from matplotlib.pyplot import ylabel, plot, show, xlabel, title
from math import log10
from math import exp
from math import factorial
x = [2, 4, 6, 8, 10, 12]
y = [log10(2), log10(4), log10(6), log10(8), log10(10), log10(12)]
x = [2, 4, 6, 8, 10, 12]
y = [exp(2), exp(4), exp(6), exp(8), exp(10), exp(12)]
x = [2, 4, 6, 8, 10, 12]
y = [factorial(2), factorial(4), factorial(6), factorial(8), factorial(10), factorial(12)]
x = [2, 4, 6, 8, 10, 12]
y = [4, 16, 36, 64, 100, 144]

plot(x, y, 'b')
xlabel('Inputs')
ylabel('Steps')
title('Constant Complexity')
show()
