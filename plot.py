import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
style.use("ggplot")
from sklearn import svm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array([[1,2,3],
             [5,8,6],
             [1.5,1.8, 2.1],
             [8,8, 8],
             [1,0.6, 0.4],
             [9,11, 13]])

y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', C = 1.0)

clf.fit(X,y)

#Used to get the hyperplane
w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]
zz = a * xx - clf.intercept_[0] / w[1]

h0 = ax.plot(xx, yy, zz,'k-', label="non weighted div")

ax.scatter(X[:, 0], X[:, 1], X[:,2], c = y)
plt.legend()
plt.show()
