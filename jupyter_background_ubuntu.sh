#!/bin/bash

USER_NAME=`whoami`
CHECK=`pgrep -f jupyter -u "$USER_NAME"`

if [ "$1" = "on" ];then
  if [ -z "$CHECK" ];then
    echo "Jupyter Notebook has been started on background."
    nohup jupyter-notebook 1>/dev/null 2>&1 &
  elif [ -n "$CHECK" ];then
    echo "Jupyter notebook is Already Runing!"
  fi

elif [ "$1" = "off" ];then
  kill $CHECK

elif [ "$1" = "ch" ];then
  if [ -z "$CHECK" ];then
    echo "Jupyter notebook is not Runing!"
  elif [ -n "$CHECK" ];then
    echo "Jupyter notebook is Runing!"
  fi
fi
