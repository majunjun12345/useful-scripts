#!/bin/bash
nodes=$(cat ips.txt)

echo "Prepare to execute ssh-copy-id on $nodes"

for ip in $nodes ; do
    echo $ip ---------------------------
    ssh-copy-id -o GSSAPIAuthentication=no root@$ip
    if [ "$?" != "0" ]; then
        break
    fi  
done