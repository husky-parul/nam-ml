from blacklisted_ip import BlackListedIP
from benign_ip import BenignIP
from training_algorithm import Intution
import utilities as utils
from model import Model
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn import svm
import matplotlib.pyplot as plt





def main():
    print 'inside main'
    evil_ipos = utils.getIpDict('blacklisted_ip.ser')
    benign_ipos = utils.getIpDict('22AprShodan_full.ser')


    intution = Intution(evil_ipos, benign_ipos)
    intution.black_listed_ips=evil_ipos
    intution.benign_ips=benign_ipos
    x,y=intution.getDataSet(evil_ipos,benign_ipos)
    X = np.array(x)
    Y = np.array(y)
    clf = SVC(kernel='linear', C=1)
    scores = cross_val_score(clf, x, y, cv=5)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    print '-------------------------------------------------------------------------------------'
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4, random_state = 3)
    print X_train.shape, y_train.shape
    print X_test.shape, y_test.shape
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    print clf.score(X_test, y_test)

    print '-------------------------------------------------------------------------------------'
    clf = svm.SVC(kernel='linear', C=1,probability=True, random_state=3)
    print cross_val_score(clf, X, y, scoring='neg_log_loss')
    model = svm.SVC()

    print cross_val_score(model, X, Y, scoring='neg_mean_squared_error')

    # Used to get the hyperplane

    # fig = plt.figure()
    # print 'clf: ',clf
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
    # plt.legend()
    # plt.show()












if __name__ == '__main__':
    main()