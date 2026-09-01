from sklearn.decomposition import PCA

n = int(input("Enter number of samples: "))
d = int(input("Enter number of features: "))

X = []

for i in range(n):
    X.append(list(map(float, input("Enter features: ").split())))

k = int(input("Enter reduced dimensions: "))

pca = PCA(n_components=k)
result = pca.fit_transform(X)

print("Reduced Data:")
print(result)
