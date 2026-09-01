from sklearn.svm import SVC

n = int(input("Enter number of samples: "))
X, y = [], []

for i in range(n):
    a, b = map(float, input("Enter 2 features: ").split())
    c = int(input("Enter class (0/1): "))
    X.append([a, b])
    y.append(c)

model = SVC(kernel='linear')
model.fit(X, y)

a, b = map(float, input("Enter test values: ").split())
print("Predicted class:", model.predict([[a, b]])[0])
