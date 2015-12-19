import numpy as np
from sklearn import mixture

np.random.seed(1)
g = mixture.GMM(n_components=2)

# Generate random observations with two modes centered on 0
# and 10 to use for training.
obs = np.concatenate((np.random.randn(100, 1),
                      10 + np.random.randn(300, 1)))
res = g.fit(obs)
print "Fit result"
print res
print

print "Weights rounded:", np.round(g.weights_, 2)
print "Means rounded:", np.round(g.means_, 2)
print "Covars rounded:", np.round(g.covars_, 2)

pred = g.predict([[0], [2], [9], [10]])
print "Predictions:", pred
print "Scores:", np.round(g.score([[0], [2], [9], [10]]), 2)

# Refit the model on new data (initial parameters remain the
# same), this time with an even split between the two modes.
res2 = g.fit(20 * [[0]] + 20 * [[10]])
print "Refit result"
print res
print "New weights:", np.round(g.weights_, 2)
