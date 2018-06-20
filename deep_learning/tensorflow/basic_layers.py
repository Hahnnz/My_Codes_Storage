import tensorflow as tf

def conv(data, ksize, filters, ssize, padding, use_bias, conv_name=None, bn_name=None, bn=False, act=True):
    if not bn :
        if act : 
            output = tf.layers.conv2d(data, kernel_size=ksize, filters=filters,
                                      strides=(ssize,ssize),
                                      padding=padding,
                                      name=conv_name, 
                                      activation=tf.nn.relu,use_bias=use_bias,
                                      kernel_initializer=tf.contrib.layers.xavier_initializer())
        else : 
            output = tf.layers.conv2d(data, kernel_size=ksize, filters=filters,
                                      strides=(ssize,ssize),
                                      padding=padding,
                                      name=conv_name,use_bias=use_bias,
                                      kernel_initializer=tf.contrib.layers.xavier_initializer())
    else : 
        conv = tf.layers.conv2d(data, kernel_size=ksize, filters=filters,
                                strides=(ssize,ssize),
                                padding=padding,
                                name=conv_name,use_bias=use_bias,
                                kernel_initializer=tf.contrib.layers.xavier_initializer())
        with tf.variable_scope(bn_name) as bn_name:
            output = tf.contrib.layers.batch_norm(conv)
        if act : output = tf.nn.relu(output)
    return output

def max_pooling(data, ksize, ssize, name=None):
    return tf.nn.max_pool(data, ksize=[1,ksize,ksize,1], strides=[1,ssize,ssize,1], padding="SAME", name=name)

def dropout(data, name=None):
    return tf.nn.dropout(data, 0.5, name=name)

def lrn(data, depth_radius, alpha, beta, name=None):
    return tf.nn.local_response_normalization(data, depth_radius=depth_radius, alpha=alpha, beta=beta, bias=1.0, name=name)

def bn(data, name=None):
    with tf.variable_scope(name) as name:
        batch_norm = tf.contrib.layers.batch_norm(data)
    return batch_norm

def fc(data, num_in, num_out, name=None, relu=True):
    with tf.variable_scope(name) as scope:
        weights = tf.get_variable('weights', shape=[num_in, num_out], trainable=True)
        biases = tf.get_variable('biases', [num_out], trainable=True)
        output = tf.nn.xw_plus_b(data, weights, biases, name=scope.name)
    if relu : 
        return tf.nn.relu(output)
    else: 
        return output
