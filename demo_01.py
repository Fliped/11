import sys
import logging
import modbus_tk 
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import time

SERVER = modbus_tcp.TcpServer(address="0.0.0.0", port=502) # 这里address如果填写127.0.0.1,就只能通过本地127.0.0.1连接，而不能通过局域网IP地址链接，可以用这个命令查看是否侦听端口:netstat -napt

# 服务启动
SERVER.start()
# 建立第一个从机
SLAVE1 = SERVER.add_slave(1)
SLAVE1.add_block('A', cst.READ_COILS, 0, 4)

for i in range(30):
    SLAVE1.set_values('A', 0, 65536)  # 改变在地址0处的寄存器的值
    time.sleep(1)
    SLAVE1.set_values('A', 0, 0)
    time.sleep(1)

master = modbus_tcp.TcpMaster(host="192.168.10.194",port=502)  #这里的ip地址填写服务端的地址
master.set_timeout(5.0)
Hold_value = master.execute(slave=1, function_code=cst.READ_COILS, starting_address=0, quantity_of_x=1)
print(Hold_value)