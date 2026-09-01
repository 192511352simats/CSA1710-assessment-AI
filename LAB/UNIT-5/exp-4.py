from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

X = [[1,2],[2,3],[3,4],[7,8],[8,9],[9,10]]
y = [0,0,0,1,1,1]

k = int(input("Enter maximum K: "))

model = GridSearchCV(
    KNeighborsClassifier(),
    {'n_neighbors': range(1, k+1)},
    cv=2
)

model.fit(X, y)

print("Best K:", model.best_params_['n_neighbors'])
print("Best Score:", model.best_score_)
