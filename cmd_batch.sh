#!/bin/bash
nodes=$(cat ips.txt)

cmd=$*
if [ -z $cmd ]; then
    echo "Usage: $0 {cmd}"
    exit 1
fi
echo "Prepare to execute $cmd on $nodes"

for ip in $nodes ; do
    echo
    echo $ip ---------------------------
    ssh -t -o GSSAPIAuthentication=no root@$ip "$cmd"
    if [ "$?" != "0" ]; then
        break
    fi  
done
