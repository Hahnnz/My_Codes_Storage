import numpy as np

def normalize_img_channel(img):
    tmp_shape = img.shape
    img = img.astype(np.float32)
    img -= img.reshape(-1, 3).mean(axis=0)
    img /= img.reshape(-1, 3).std(axis=0) + 1e-5
    img = img.reshape(tmp_shape)
return img
