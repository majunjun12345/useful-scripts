import os
import time
import json

CONF_PATH = '/etc/docker/daemon.json'
CONF = { "registry-mirrors": ["https://registry.docker-cn.com"] }

# already exists
if os.path.exists(CONF_PATH):
    OLD_CONF = json.loads(open(CONF_PATH).read())
    OLD_CONF.update(CONF)
    CONF = OLD_CONF

print json.dumps(CONF, indent=2)
choice = raw_input('comfirm this? [y/n]').lower()
if choice != 'y':
    print 'exit...'
else:
    if os.path.exists(CONF_PATH):
        bak = '/etc/docker/daemon.json.%s' % int(time.time())
        os.system('cp %s %s' % (CONF_PATH, bak))
    open(CONF_PATH, 'wb').write(json.dumps(CONF))
    print 'save to %s' % CONF_PATH
    print 'then you should systemctl restart docker...'
