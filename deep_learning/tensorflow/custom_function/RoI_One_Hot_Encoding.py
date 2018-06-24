def RoI_OHE(roi_mask,Class):
    """
    Description
        Region Of Interest One How Encoding (Tensor). This function is suitted for PNDC-project only.
        
    Arguments
        - roi_mask : roi mask data (512,512,3)
        - Class : insert 'Benign' or 'Malignant'
    
    Output
        one hot encoded roi mask
    """
    if Class.lower() == "benign": Class = tf.constant([0,1,0])
    elif Class.lower() == "malignant": Class = tf.constant([0,0,1])
    else : raise ValueError("Class should 'Benign' or 'Malignant'.")
    
    one_hot_roi = None
    roi_x, roi_y = list(map(int,test_roi.get_shape()))[:2]
    for i in range(roi_x):
        one_hot = tf.map_fn(lambda x: 
                                tf.cond(tf.greater(x[0],0), 
                                        lambda: Class, lambda: tf.constant([1,0,0])),
                                roi_mask[i])
        if i == 0 :
            one_hot_roi=tf.expand_dims(one_hot,0)
        else :
            one_hot_roi = tf.concat((one_hot_roi,tf.expand_dims(one_hot,0)),axis=0)
        
    return one_hot_roi