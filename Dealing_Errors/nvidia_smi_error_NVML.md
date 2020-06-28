# NVIDIA Driver Error

## Error : Failed to initialize NVML: Driver/library version mismatch
1. Unload `nvidia-drm` kernel module.
```
$ sudo rmmod nvidia_drm
$ sudo rmmod nvidia_modeset
$ sudo rmmod nvidia_uvm
$ sudo rmmod nvidia
```

- if you got the error `rmmod: ERROR: Module nvidia is in use` , kill the processors that use GPU.
> if the first command doesn't work, then command below one.
```
$ sudo lsof /dev/nvidia*
$ sudo systemctl isolate multi-user.target
```

2. Retype the command `nvidia-smi`. or reboot. then it will work.
