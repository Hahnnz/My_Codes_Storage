import tensorflow as tf

def ZeroPadding2D(data,psize,Type="CONSTANT",name=None):
    data_shape=data.get_shape().as_list()
    if data_shape[0]==None :
        raise ValueError("batch_size must be specified.")
    else:
        paddings = tf.constant([psize, psize])
        for batch_size in range(data_shape[0]):
            padded = tf.pad(data[0,:,:,0],paddings,Type)
            padded = tf.expand_dims(tf.expand_dims(padded,axis=0),axis=3)

            for channels in range(1,data_shape[3]):
                padded_2 = tf.pad(data[0,:,:,channels],paddings,Type)
                padded_2 = tf.expand_dims(tf.expand_dims(padded_2,axis=0),axis=3)
                padded = tf.concat([padded,padded_2],3)

            if batch_size==0 :
                padded_dataset=padded
            else :
                padded_dataset=tf.concat([padded_dataset,padded],0)
    return padded_dataset
