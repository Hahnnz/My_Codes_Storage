import numpy

def _one_hot_encoding(labels):
    return np.eye(np.max(labels) + 1)[labels].reshape(labels.shape[0],np.max(labels) + 1)
