import numpy as np
import scipy as sp
from scipy import sparse, linalg, stats
from tqdm import tqdm

def TGA(X, n_components=1, p=0.49999, eps=1e-5):
    '''
    An implementation of the trimmed grassman average
    for robust principal component analysis
    outlined in "Grassmann Averages for Scalable Robust PCA"
    Parameters
    ----------
        X:  Input data matrix
        p:  Argument to scipy.stats.trim_mean
        n_components:  The number of components to compute
    Returns
    -------
        n_components of robust components
    '''
    assert(len(X.shape) == 2)

    m,n = X.shape

    # Calculate the means and subtract them
    # from the data matrix
    #means = np.mean(X, axis=0)
    #X -= means

    vectors = np.zeros(n_components*n, dtype=X.dtype).reshape((n_components,n))
    
    with tqdm(total=n_components) as pbar:
        pbar.set_description('[ Trimmed grassman average for Scalable Robust PCA ]')
        for i in range(n_components):
            mu = np.random.rand(n) - 0.5
            mu /= np.linalg.norm(mu)

            for _ in range(3):
                dots = np.dot(X, mu)
                mu = np.dot(dots.T, X)
                mu /= np.linalg.norm(mu)

            for j in range(m):
                prev_mu = mu

                dot_signs = np.sign(np.dot(X, mu))

                mu = sp.stats.trim_mean(X.T * dot_signs, p, axis=1)
                mu /= np.linalg.norm(mu)+1e-17

                if np.max(np.abs(mu - prev_mu)) < eps:
                    break

            if i == 0:
                vectors[i] = mu
                #X = X - np.dot(mu, np.dot(X, mu).T)
                X -= np.dot(np.dot(X, mu).reshape((-1,1)), mu.reshape((1,-1)))
            elif i < n_components:
                # should reorthogonalize mu to the existing basis like:
                # mu = reorth(vectors[:i], mu)
                # mu /= np.linalg.norm(mu)
                # for numerical stability (but mu should already be orthogonal)
                vectors[i] = mu
                #X = X - np.dot(mu, np.dot(X, mu).T)
                X -= np.dot(np.dot(X, mu).reshape((-1,1)), mu.reshape((1,-1)))
            else:
                # should reorthogonalize mu to the existing basis like:
                # mu = reorth(vectors[:i], mu)
                # mu /= np.linalg.norm(mu)
                # for numerical stability (but mu should already be orthogonal)
                vectors[i] = mu
            
    return vectors