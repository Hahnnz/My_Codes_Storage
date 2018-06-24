import tensorflow as tf

def PixelWiseSoftmax_with_Loss(logits, num_classes, mask):
    """
    Description
        Compute Softmax_with_Loss pixel by pixel
        
    Arguments
        - logits : Output of network
        - num_classes : number of Classes 
        - mask : mask labels
    
    Output
        Loss of for output of network
    """
    logits = tf.reshape(logits, (-1, num_classes))
    mask = tf.reshape(mask, [-1])
    cross_entorpy = tf.nn.sparse_softmax_cross_entrophy_with_logits(logits, mask)
    return tf.reduce_mean(cross_entrophy)
