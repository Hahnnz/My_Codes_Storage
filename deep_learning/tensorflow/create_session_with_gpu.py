import tensorflow as tf

def create_session_with_gpu(gpu_memory_fraction=None):
    config = tf.ConfigProto(log_device_placement=False, allow_soft_placement=True)
    if gpu_memory_fraction is None:
        config.gpu_options.allow_growth = True
    else:
        config.gpu_options.per_process_gpu_memory_fraction = gpu_memory_fraction

    return tf.Session(config=config)
