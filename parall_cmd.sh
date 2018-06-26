#!/bin/bash
nodes=$(cat ips.txt)

cmd="$*"
if [ -z "$cmd" ]; then
    echo "Usage: $0 {cmd}"
    exit 1
fi
echo "Prepare to execute $cmd on $nodes"

for ip in $nodes ; do
    echo $ip ---------------------------
    ssh -o GSSAPIAuthentication=no root@$ip "$cmd" &
done