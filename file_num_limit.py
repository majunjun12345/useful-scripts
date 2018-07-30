# -*- coding:utf-8 -*-

import os
import sys
import glob

KEEP_NUM = 10
FILENAME_PREFIX = 'S3-'

files = glob.glob('%s*' % FILENAME_PREFIX)
if len(files) <= KEEP_NUM:
    sys.exit(0)

sorted_files = sorted(files)
rm_files = sorted_files[0:len(files)-KEEP_NUM]
for file in rm_files:
    os.remove(file)


