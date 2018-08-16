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


# cmd_batch.sh / scp_batch.sh
多台机器批量执行命令或复制数据

示例:
> 创建一个包含IP 列表的`ips.txt` 文件
```
192.168.1.80
192.168.1.81
192.168.1.82
```
> 执行命令
```
bash cmd_batch.sh date
bash scp_batch.sh /tmp/test.txt /tmp
```

# install_docker_parall.sh
多台机器中并行安装docker
示例:
> 创建一个包含IP 列表的`ips.txt` 文件
```
192.168.1.48
192.168.1.53
192.168.1.54
```
> 执行命令
```
bash install_docker_parall.sh
```
> 验证
```
bash cmd_batch.sh docker
```
> 启动
```
bash cmd_batch.sh "systemctl start docker"
```
> 运行状态
```
bash cmd_batch.sh "systemctl status docker"
```
> 自启动状态
```
bash cmd_batch.sh "systemctl enable docker"
```

# aws_ec.py
远程启动或关闭aws 上的ec 服务器，需要提供服务器ID，访问秘钥对

> 启动
```
python aws_ec.py start
```

> 关闭
```
python aws_ec.py stop
```
