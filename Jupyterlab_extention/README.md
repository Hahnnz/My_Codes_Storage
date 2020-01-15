# Jupyterlab Extention Environment for me

Jupyterlab Extention Setting 

## 0. Prerequisites
```
$ sudo apt install -y nodejs npm
$ pip3 install nodejs npm
```

## 1. [JupyterLab Top Bar](https://github.com/jtpio/jupyterlab-topbar)

Monorepo to experiment with the top bar space in JupyterLab.<br>
Similar to the status bar, the top bar can be used to place a few indicators and optimize the overall space.<br>
Inspired by Gnome Shell Top Bar indicators.

```
$ jupyter labextension install jupyterlab-topbar-extension \
                               jupyterlab-system-monitor \
                               jupyterlab-topbar-text \
                               jupyterlab-logout \
                               jupyterlab-theme-toggle
```











# Final line you have to run to apply those extensions
```
$ jupyter lab build
```
