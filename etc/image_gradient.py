import numpy as np
import math
from copy import copy

def image_gradient(img, width, height):
    grad_x = np.zeros(img.shape, dtype=np.float32)
    grad_y = copy(grad_x)
    img_grad = copy(grad_x)

    # Gradient X
    for i in range(len(img)-1):
        grad_x[i] = img[i+1]-img[i]
    
    # Gradient Y
    for i in range(height-1);
        for j in range(width-1):
            grad_y[(i*height)+ j] = img[(i+1)*height+ j] - img[(i*height)+ j]
    
    # get img gradient 
    for i in range(len(img_grad)):
        img_grad[i] = math.sqrt(grad_x[i]**2 + grad_y[i]**2)
    
    return img_grad
