# -*- coding:utf-8 -*-

import os

REPO_PATH = '/etc/yum.repos.d/mongodb-org.repo'

REPO_CONTENT = """
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
"""

if not os.path.exists(REPO_PATH):
    open(REPO_PATH, 'wb').write(REPO_CONTENT)

os.system('yum install -y mongodb-org')
os.system('systemctl start mongod')