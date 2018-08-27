# How to add another kernel into jupyter notebook?

### 1. Python 2
```
$ pip2 install --user ipykernel
$ python2 -m ipykernel install --user
```

### 2. Cpp
Cpp interpreter : https://root.cern.ch/download/cling/
```
In Ubuntu 16.xx
$ wget https://root.cern.ch/download/cling/cling_2018-04-19_ubuntu16.tar.bz2
$ export PATH=/mypath/cling_2018-04-19_ubuntu16/bin:$PATH

In OSX
$ wget https://root.cern.ch/download/cling/cling_2018-04-19_mac1012.tar.bz2
$ export PATH=/mypath/cling_2018-04-19_mac1012/bin:$PATH

-----------------------------------------------------------------------------

$ cd share/cling/Jupyter/kernel/
$ pip install --user -e .
$ jupyter-kernelspec install --user cling-cpp17
```
