# -*- coding: utf-8 -*-
# 0 1 * * * cd /data/cron && python backup_mongo.py

import os
import time
import glob

mongo_host = '127.0.0.1:27017'
databases = ['db1']
backup_dir = '/data/backup/mongod'
log_path = '/data/backup/mongod/backup.log'
mongodump_bin_path = '/usr/local/mongodb/bin/mongodump'
backup_limit = 10

def log(msg):
    with open(log_path, 'a+') as f:
        f.write('%s\n' % msg)

def backup(name):
    backup_name = '%s_meta_%s.gz' % (name, time.strftime('%Y-%m-%d', time.gmtime()))
    backup_file_path = os.path.join(backup_dir, backup_name)
    backup_cmd = '%s -h %s -d %s --gzip --archive=%s' % (mongodump_bin_path, mongo_host, name, backup_file_path)
    code = os.system(backup_cmd)
    if code != 0:
        log('backup %s failed, %s, %s' % (backup_name, code, time.ctime()))
    else:
        log('backup %s success, %s, %s' % (backup_name, code, time.ctime()))

def limit(name):
    files = glob.glob('%s_meta_*' % name)
    if len(files) <= backup_limit:
        return

    sorted_files = sorted(files)
    rm_files = sorted_files[0:len(files)-backup_limit]
    for file in rm_files:
        os.remove(file)

for name in databases:
    backup(name)
    limit(name)

print 'done'
