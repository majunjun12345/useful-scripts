import os

STABLE_NAME = 'hadoop-3.2.0.tar.gz'
STABLE_URL = 'http://mirror.bit.edu.cn/apache/hadoop/common/stable/%s' % STABLE_NAME
YUMS = ['java-1.8.0-openjdk', 'java-1.8.0-openjdk-devel', 'rsync', 'wget']
OP_HOME = '_hadoop_op_'
INSTALL_HOME = '/opt'
os.system('mkdir -p %s' % OP_HOME)
os.chdir(OP_HOME)

def must_run(cmd):
    assert os.system(cmd) == 0, 'run %s error.' % cmd
    print 'run %s done.' % cmd

cmds = [
    'yum install -y %s' % ' '.join(YUMS),
    'wget %s' % STABLE_URL,
    'tar -xvf %s -C %s' % (STABLE_NAME, INSTALL_HOME),
]
map(must_run, cmds)

os.chdir(INSTALL_HOME)
must_run('ln -snf %s hadoop' % STABLE_NAME.strip('.tar.gz'))

HADOOP_HOME = os.path.join(INSTALL_HOME, 'hadoop')
os.chdir(HADOOP_HOME)
cmds = [
    "sed -i -e 's/# export JAVA_HOME=/export JAVA_HOME=\/usr\/lib\/jvm\/jre/g' etc/hadoop/hadoop-env.sh",
    'bin/hadoop version'
]
must_run(cmds)
print 'Done.'
