#!/bin/sh

sudo iptables -t nat -A POSTROUTING -o enp0s25 -j MASQUERADE
sudo iptables -A FORWARD -i enp32s0 -o enp0s25 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i enp0s25 -o enp32s0 -j ACCEPT
