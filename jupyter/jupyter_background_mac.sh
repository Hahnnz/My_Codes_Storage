#!/bin/bash

CHECK=`pgrep -fl jupyter`

if [ "$1" = "on" ];then
  if [ -z "$CHECK" ];then
    echo "Jupyter Notebook has been started on background."
    source ~/env/python3-jp/bin/activate
    nohup jupyter-notebook 1>/dev/null 2>&1 &
  elif [ -n "$CHECK" ];then
    echo "Jupyter notebook is Already Runing!"
  fi

elif [ "$1" = "off" ];then
  kill `pgrep -fn jupyter`

elif [ "$1" = "ch" ];then
  if [ -z "$CHECK" ];then
    echo "Jupyter notebook is not Runing!"
  elif [ -n "$CHECK" ];then
    echo "Jupyter notebook is Runing!"
  fi
fi
