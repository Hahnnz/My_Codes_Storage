import numpy as np
import sys, argparse
caffe_root = './caffe/' 
sys.path.insert(0, caffe_root + 'python')
import caffe
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata

caffe.set_mode_cpu()

mnist = fetch_mldata('MNIST original')
X, y = mnist["data"], mnist["target"]

def classify(idx):
	digit = np.array(X[idx].reshape(28, 28))
	digit=digit[np.newaxis,np.newaxis,:,:]

	model='./caffe/examples/mnist/lenet.prototxt'
	pretrained='./caffe/examples/mnist/lenet_iter_10000.caffemodel'
	net = caffe.Net(model, pretrained, caffe.TEST)
	net.blobs['data'].data[0]=digit
	return net.forward()

def parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("index", type=int, help = "type the index of mnist dataset")
	return parser.parse_args().index

if __name__ == "__main__":
	result=classify(parser())
	plt.imshow(np.array(X[parser()].reshape(28, 28)), cmap = matplotlib.cm.binary,interpolation="nearest")
	plt.axis("off")
	plt.text(1,1,"Predicted : "+str(list(result["prob"][0]).index(1)), fontsize=20)
	plt.text(1,3,"Target Label : "+str(int(y[parser()])), fontsize=20)
	plt.show()
