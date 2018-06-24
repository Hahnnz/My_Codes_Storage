# Intersection over Union Loss

import tensorflow as tf

def IoU_Loss(logits, num_classes, mask):
    """
    Description
        Compute loss by how much pixels net output and mask are overlapping each other
        
    Arguments
        - logits : Output of network
        - num_classes : number of Classes 
        - mask : mask labels
    
    Output
        Loss of for output of network
    """
    
    logits = tf.reshape(logits, (-1, num_classes))
    mask = tf.reshape(mask, [-1])

    inter = tf.reduce_sum(tf.multiply(logits, mask))
    union = tf.reduce_sum(tf.subtract(tf.add(logits, mask), tf.multiply(logits, mask)))

    return tf.substract(tf.constant(1.0, dtype=tf.float32), tf.div(interm union))
