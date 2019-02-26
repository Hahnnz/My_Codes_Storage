# How to install R on Ubuntu 16.04?
```
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
$ sudo add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'
$ sudo apt-get update
$ sudo apt install r-base
```

# How to install R-Studio on Ubuntu 16.04?
```
$ sudo apt install gdebi-core
$ wget https://download1.rstudio.org/rstudio-1.0.44-amd64.deb
$ sudo gdebi rstudio-1.0.44-amd64.deb
```
