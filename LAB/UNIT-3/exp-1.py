from sklearn.linear_model import LinearRegression

n = int(input("Enter number of data points: "))
X, y = [], []

for i in range(n):
    x = float(input("Enter X: "))
    z = float(input("Enter Y: "))
    X.append([x])
    y.append(z)

model = LinearRegression()
model.fit(X, y)

x = float(input("Enter X to predict: "))
print("Predicted Y:", model.predict([[x]])[0])
