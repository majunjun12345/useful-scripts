#/bin/bash

cmd="cd /tmp && curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh"
bash parall_cmd.sh $cmd