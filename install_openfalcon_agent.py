import os
import sys
import json

DOWNLOAD_URL = 'http://61.155.138.173:11580/open-falcon/linux_agent_x64.tar.gz'
# DOWNLOAD_URL = 'http://192.168.122.15/open-falcon/linux_agent_x64.tar.gz'

INSTALL_HOME = '/data/monitor'
APP_HOME = os.path.join(INSTALL_HOME, 'linux_agent_x64')

heartbeat_addr = '123.155.154.203:50136'
transfer_addr = '123.155.154.203:60136'
assert len(sys.argv) == 2, "unique hostname needed"
hostname = sys.argv[1]

# install
os.system('mkdir -p %s' % INSTALL_HOME)
code = os.system('curl %s > /tmp/linux_agent_x64.tar.gz && tar -xvf /tmp/linux_agent_x64.tar.gz -C %s' % (DOWNLOAD_URL, INSTALL_HOME))
assert code == 0, "install failed"

# config
cfg_path = os.path.join(APP_HOME, 'agent/config/cfg.json')
config = json.loads(open(cfg_path).read())
config['hostname'] = hostname
config['heartbeat']['addr'] = heartbeat_addr
config['transfer']['addr'] = transfer_addr
open(cfg_path, 'wb').write(json.dumps(config, indent=4))

# autorun
seted = False
runcmd = 'cd %s && ./open-falcon start agent' % APP_HOME
for rc in ['/etc/rc.local', '/etc/rc.d/after.local']:
    if not os.path.exists(rc):
        continue
    assert os.system('echo "%s" >> %s' % (runcmd, rc)) == 0
    assert os.system('chmod +x %s' % rc) == 0
    seted = True
assert seted, "autorun failed"

# start
os.system(runcmd)
