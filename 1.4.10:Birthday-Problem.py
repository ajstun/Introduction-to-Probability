import math
import matplotlib.pyplot as plt

n = 365
k_max = 101

k = range(1, k_max) 


prob = []
prob_complement = []
k_values = []

def run_permutation(k):
	numerator = math.prod(range(n, n-k, -1))
	denominator = n**k

	prob.append(numerator/denominator)
	prob_complement.append(1 - (numerator/denominator))
	k_values.append(k)

for x in k:
	run_permutation(x)


plt.plot(k_values, prob)
plt.plot(k_values, prob_complement)
plt.show()


