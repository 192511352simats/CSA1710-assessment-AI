from sklearn.tree import DecisionTreeClassifier

n = int(input("Enter number of samples: "))
X = []
y = []

for i in range(n):
    a = list(map(int, input("Enter features: ").split()))
    X.append(a)
    y.append(int(input("Enter class (0/1): ")))

model = DecisionTreeClassifier()
model.fit(X, y)

test = list(map(int, input("Enter test features: ").split()))
print("Predicted class:", model.predict([test])[0])
