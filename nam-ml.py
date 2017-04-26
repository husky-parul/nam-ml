from training_algorithm import Intution
import utilities as utils
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import constants as CN

def predictAndPlotThreeFeatures(intution):

    x,y=intution.getDataSet()
    X = np.array(x)
    Y = np.array(y)

    print '--------------------PREDICT AND PLOT THREE FEATURES----------------------------------'
    clf = SVC(kernel=CN.LINEAR, C=1)
    scores = cross_val_score(clf, x, y, cv=5)
    print 'Splited dataset score for 5 iterations: ',scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    print '-------------------------------------------------------------------------------------'
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4, random_state = 3)
    clf = svm.SVC(kernel=CN.LINEAR, C=1).fit(X_train, y_train)
    print 'Randomly splited dataset score with test size of 40%: ',clf.score(X_test, y_test)

    print '-------------------------------------------------------------------------------------'
    clf = svm.SVC(kernel=CN.LINEAR, C=1,probability=True, random_state=3)
    print 'NEG_LOG_LOSS: ',cross_val_score(clf, X, y, scoring=CN.NEG_LOG_LOSS)
    print 'NEG_MEAN_SQUARED_ERROR: ',cross_val_score(clf, X, Y, scoring=CN.NEG_MEAN_SQUARED_ERROR)

    print '----------------------------------------------------------------------'


    # Used to get the hyperplane with complete dataset

    fig = plt.figure()
    ax = fig.add_subplot(111, projection=CN.THREE_D_PROJECTION)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
    plt.legend()
    plt.show()

def predictAndPlotOneFeature(intution):

    x, y = intution.getDataSetWithOneFeature()
    X = np.array(x)
    Y = np.array(y)

    clf = SVC(kernel=CN.LINEAR, C=1)

    plt.scatter(X, Y)
    plt.show()

def predictAndPlotTwoFeature(intution):

    x, y = intution.getDataSetWithTwoFeatures()
    X = np.array(x)
    Y = np.array(y)

    print '--------------------PREDICT AND PLOT TWO FEATURES----------------------------------'
    clf = SVC(kernel=CN.LINEAR, C=1)
    scores = cross_val_score(clf, x, y, cv=5)
    print 'Splited dataset score for 5 iterations: ', scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    print '-------------------------------------------------------------------------------------'
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=3)
    clf = svm.SVC(kernel=CN.LINEAR, C=1).fit(X_train, y_train)
    print 'Randomly splited dataset score with test size of 40%: ', clf.score(X_test, y_test)

    print '-------------------------------------------------------------------------------------'
    clf = svm.SVC(kernel=CN.LINEAR, C=1, probability=True, random_state=3)
    print 'NEG_LOG_LOSS: ', cross_val_score(clf, X, y, scoring=CN.NEG_LOG_LOSS)
    print 'NEG_MEAN_SQUARED_ERROR: ', cross_val_score(clf, X, Y, scoring=CN.NEG_MEAN_SQUARED_ERROR)

    print '----------------------------------------------------------------------'

    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.legend()
    plt.show()

def main():
    evil_ipos = utils.getIpDict(CN.BLACKLISTED_IP_SER)
    benign_ipos = utils.getIpDict(CN.SHODAN_FULL_SER)

    intution = Intution(evil_ipos, benign_ipos)
    intution.black_listed_ips = evil_ipos
    intution.benign_ips = benign_ipos

    predictAndPlotOneFeature(intution)
    predictAndPlotTwoFeature(intution)
    predictAndPlotThreeFeatures(intution)


if __name__ == '__main__':
    main()