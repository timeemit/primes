import numpy as np
import matplotlib.pyplot as plt


primes = np.array([2,3,5,7,11,13,17,19,23,29,31,37])
theta = primes / np.log(primes) * 2 * np.pi / 16

ax = plt.subplot(111, projection='polar')
ax.plot(theta, primes)
exponents = np.arange(1, 4)
for i, prime in enumerate(primes[:4]):
    prime_exponents = prime ** exponents
    # thetas = theta[i] - theta[:6]
    # thetas = - theta[i] * np.arange(1,7)
    thetas = theta[i] - np.arange(0,3) / prime 
    ax.plot(thetas, prime_exponents)

ax.set_rmax(50)
# ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
# ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
