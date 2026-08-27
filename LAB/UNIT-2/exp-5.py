import numpy as np
from sklearn.neural_network import MLPClassifier

n = int(input("Enter number of samples: "))
X = []
y = []

for i in range(n):
    X.append(list(map(float, input("Enter input values: ").split())))
    y.append(int(input("Enter output: ")))

model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000)
model.fit(X, y)

test = list(map(float, input("Enter test input: ").split()))
print("Predicted output:", model.predict([test])[0])
