#!/bin/bash
read -p "Enter the domain name or IP address: " arg
traceroute $arg  > trace.txt