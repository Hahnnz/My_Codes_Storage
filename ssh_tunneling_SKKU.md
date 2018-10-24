# SSH Tunneling for SKKU-HPC Servers

## Client [My PC]

> $ ssh USERNAME@[SKKU-HPC Server Address] -p 22  -N -L 5001:xxx.xxx.xxx.11:5001 -L 5002:xxx.xxx.xxx.12:5002 -L 5003:xxx.xxx.xxx.13:5003 -L 5004:xxx.xxx.xxx.14:5004 -L 5005:xxx.xxx.xxx.15:5005 -L 5006:xxx.xxx.xxx.16:5006 -L 5007:xxx.xxx.xxx.17:5007 -L 5008:xxx.xxx.xxx.18:5008 -L 5009:xxx.xxx.xxx.19:5009 -L 5010:xxx.xxx.xxx.20:5010 -L 5011:xxx.xxx.xxx.21:5011 -L 5012:xxx.xxx.xxx.22:5012 -L 5014:xxx.xxx.xxx.24:5014 -L 5015:xxx.xxx.xxx.25:5015 -L 5016:xxx.xxx.xxx.26:5016


## SKKU-HPC Hosts alias
```shell
alias jpb_[host_name_01]="nohup jupyter notebook --ip=xxx.xxx.xxx.11 --port=5001 1>/dev/null 2>&1 &"
alias jpb_[host_name_02]="nohup jupyter notebook --ip=xxx.xxx.xxx.12 --port=5002 1>/dev/null 2>&1 &"
alias jpb_[host_name_03]="nohup jupyter notebook --ip=xxx.xxx.xxx.13 --port=5003 1>/dev/null 2>&1 &"
alias jpb_[host_name_04]="nohup jupyter notebook --ip=xxx.xxx.xxx.14 --port=5004 1>/dev/null 2>&1 &"
alias jpb_[host_name_05]="nohup jupyter notebook --ip=xxx.xxx.xxx.15 --port=5005 1>/dev/null 2>&1 &"
alias jpb_[host_name_06]="nohup jupyter notebook --ip=xxx.xxx.xxx.16 --port=5006 1>/dev/null 2>&1 &"
alias jpb_[host_name_07]="nohup jupyter notebook --ip=xxx.xxx.xxx.17 --port=5007 1>/dev/null 2>&1 &"
alias jpb_[host_name_08]="nohup jupyter notebook --ip=xxx.xxx.xxx.18 --port=5008 1>/dev/null 2>&1 &"
alias jpb_[host_name_09]="nohup jupyter notebook --ip=xxx.xxx.xxx.19 --port=5009 1>/dev/null 2>&1 &"
alias jpb_[host_name_10]="nohup jupyter notebook --ip=xxx.xxx.xxx.20 --port=5010 1>/dev/null 2>&1 &"
alias jpb_[host_name_11]="nohup jupyter notebook --ip=xxx.xxx.xxx.21 --port=5011 1>/dev/null 2>&1 &"
alias jpb_[host_name_12]="nohup jupyter notebook --ip=xxx.xxx.xxx.22 --port=5012 1>/dev/null 2>&1 &"
alias jpb_[host_name_14]="nohup jupyter notebook --ip=xxx.xxx.xxx.24 --port=5014 1>/dev/null 2>&1 &"
alias jpb_[host_name_15]="nohup jupyter notebook --ip=xxx.xxx.xxx.25 --port=5015 1>/dev/null 2>&1 &"
alias jpb_[host_name_16]="nohup jupyter notebook --ip=xxx.xxx.xxx.26 --port=5016 1>/dev/null 2>&1 &"
```
