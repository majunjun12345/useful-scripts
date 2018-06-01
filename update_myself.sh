#!/bin/bash                                                                                                                                                                                                        
# crontab: * * * * * bash /root/public/useful_scripts/update_myself.sh

HERE=$(dirname $(readlink -f $0))
cd $HERE

# force overwrite of local branch
git pull origin master -f