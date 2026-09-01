from sklearn.neighbors import KNeighborsClassifier

n = int(input("Enter number of samples: "))
X, y = [], []

for i in range(n):
    a, b = map(float, input("Enter 2 features: ").split())
    c = int(input("Enter class: "))
    X.append([a, b])
    y.append(c)

k = int(input("Enter K: "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

a, b = map(float, input("Enter test values: ").split())
print("Predicted class:", model.predict([[a, b]])[0])
