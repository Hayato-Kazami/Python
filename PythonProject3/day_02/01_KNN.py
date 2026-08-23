from sklearn.neighbors import KNeighborsClassifier

x = [[1],[45],[15],[-32]]
y = [0,1,0,1]
clf = KNeighborsClassifier(n_neighbors=2)
clf.fit(x,y)

print(clf.predict([[78]]))