import csv
import numpy as np
import matplotlib.pyplot as plt

# Load the factoizations
with open('./computed-data.csv') as f:
# with open('./data.csv') as f:
    reader = csv.reader(f)
    header = reader.__next__()
    primes = np.array(header, dtype=int)
    factors = np.empty((0, len(header)), dtype=int)
    labels = np.empty((0, 1), dtype=int)
    label = 1
    for row in reader:
        label += 1
        datum = np.array([row], dtype=int)
        actual = np.prod(primes ** datum)
        if actual != label:
            print("Warning: {} label but actual found {}".format(label, actual))

        factors = np.append(factors, datum, axis=0)
        labels = np.append(labels, np.array([label], dtype=int))

# Load the T-Sne positioning
result = np.empty((0, 2), dtype=float)
with open('./t-sne.csv') as f:
    for row in csv.reader(f):
        np_row = np.array([row], dtype=float)
        result = np.append(result, np_row, axis=0)

# Illustrate their relationships
fig, ax = plt.subplots()
ax.scatter(result[:, 0], result[:, 1], c="#ffffff")

for i in range(len(result)):
    txt = str(i + 2)
    if i == 0:
        ax.annotate(txt, xy=(result[i]))
        continue
    factorization = factors[i]
    num = int(txt)
    for nth_prime, power in enumerate(factorization):
        if power < 1:
            continue
        prime = int(primes[nth_prime])
        num /= prime ** power
        num *= prime ** (power - 1)
        num = int(num)
        ax.annotate(
                txt,
                xy=result[num-2], xycoords="data",
                xytext=result[i], textcoords="data",
                arrowprops=dict(
                    arrowstyle="->",
                    edgecolor="blue"
                    )
                )

plt.show()
