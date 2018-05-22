# useful_scripts

存放一些小脚本

# install_openfalcon_agent.py
主要用于在公司Linux 服务器上一键安装openfalcon agent, 默认配置的Server 地址是
openfalcon.cloudhua.com 上的openfalcon 服务。

- hostname, 用于区分不同的服务器，可以用域名或IP，具有可读性即可

命令:

```
python install_openfalcon_agent.py [hostname]
```

示例:

```
python install_openfalcon_agent.py pan.cloudhua.com
python install_openfalcon_agent.py jiangshu-61.155.138.173
```


