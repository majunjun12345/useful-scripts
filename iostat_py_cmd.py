# -*- coding: UTF-8 –*-

# 亮点：python 执行 linux 命令，如需 sudo 权限则配置密码

# 测试磁盘的 io 性能, 半小时统计一次，统计 12 次
# iostat 测试综合能力
# dd 分别测试读写能力
# 需要改变的配置有：passwd file cmd

import os
import time
import datetime


passwd = "Mj900928"
iostat_file = open("io_stat.txt", "a")
ddr_file = open("ddr_stat.txt", "a")
ddw_file = open("ddw_stat.txt", "a")

def test_io():
    print("start monitoring...")

    count = 0
    while True:
        tm = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

        cmd1 = "iostat 2 3 -d /dev/sda7"
        f_iostat = os.popen(cmd1)
        iostat_file.write(tm + "\n")
        iostat_file.write(f_iostat.read() + "\n" + "\n" + "\n")

        # 读
        cmd2 = "sudo time dd if=/dev/sda7 of=/dev/null bs=4k count=30000"
        ddr_stat = os.popen('echo %s|sudo -S %s' % (passwd, cmd2))
        ddr_file.write(tm + "\n")
        ddr_file.write(ddr_stat.read() + "\n" + "\n" + "\n")

        # 写
        cmd3 = "sudo time dd if=/dev/zero of=testw.dbf bs=4k count=30000 oflag=direct"
        ddw_stat = os.popen('echo %s|sudo -S %s' % (passwd, cmd3))
        ddw_file.write(tm + "\n")
        ddw_file.write(ddw_stat.read() + "\n" + "\n" + "\n")

        count += 1
        print(count)
        if count >= 6:
            break
        time.sleep(1800)

    print("ending monitor！")


if __name__ == "__main__":
    test_io()
