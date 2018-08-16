# coding: utf-8
# pip install boto3

import sys
import time
import boto3

ec_id = 'iiiii' # EC 服务器ID
ak = 'xxxxx' # 访问秘钥对
sk = 'yyyyy' # 访问秘钥对

boto3.setup_default_session(
    region_name='cn-north-1',
    aws_access_key_id=ak,
    aws_secret_access_key=sk,
)

ec2 = boto3.resource('ec2')
instance = ec2.Instance(ec_id)


usage = 'usage: python aws_ec.py [start|stop]'
assert len(sys.argv) == 2, usage


def wait_for(obj):
    for _ in range(10):
        if obj:
            return obj
        time.sleep(2)
    return '获取失败, 请重试'


op = sys.argv[1]
if op == 'start':
    print instance.start()['StartingInstances']
    print 'DNS:', wait_for(instance.public_dns_name)
    print 'IP:', wait_for(instance.public_ip_address)
elif op == 'stop':
    print instance.stop()['StoppingInstances']
else:
    print usage
