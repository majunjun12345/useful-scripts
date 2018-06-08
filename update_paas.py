# -*- coding:utf-8 -*-

import os

# for paas docker builder

paas_projs = ["rad", "transcoding", "docsview", "imageprocessing"]
git_cmd = "git pull origin master -f"

home = os.getcwd()
for proj in paas_projs:
    os.chdir(proj)
    os.system(git_cmd)
    os.chdir(home)
    