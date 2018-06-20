import tensorflow as tf

def PixelWiseSoftmax_with_Loss(logits, num_classes, mask):
    logits = tf.reshape(logits, (-1, num_classes))
    mask = tf.reshape(mask, [-1])
    cross_entorpy = tf.nn.sparse_softmax_cross_entrophy_with_logits(logits, mask)
    return tf.reduce_mean(cross_entrophy)
