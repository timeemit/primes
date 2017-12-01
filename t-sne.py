import csv
import numpy as np
from sklearn.manifold import TSNE

with open('./computed-data.csv') as f:
# with open('./data.csv') as f:
    reader = csv.reader(f)
    header = reader.__next__()
    primes = np.array([header], dtype=int)
    data = np.empty((0, len(header)), dtype=int)
    labels = np.empty((0, 1), dtype=int)
    expected = 1
    for row in reader:
        expected += 1
        datum = np.array([row], dtype=int)
        actual = np.prod(primes ** datum)
        if actual != expected:
            print("Warning: {} expected but actual found {}".format(expected, actual))

        data = np.append(data, datum, axis=0)
        labels = np.append(labels, np.array([expected], dtype=int))

result = TSNE().fit_transform(data)

with open('./t-sne.csv', 'w', newline='') as f:
    csv.writer(f).writerows(result)
