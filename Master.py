
import imp
import sys
import logging
import modbus_tk 
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import xlwt
import socket

modbus_ip='0.0.0.0'
Modbus_port="502"

LOGGER=modbus_tk.utils.create_logger("console")
MASTER=modbus_tcp.TcpMaster(host=modbus_ip,port=Modbus_port)
MASTER.set_timeout(5.0)
LOGGER.info("connected")

sk=socket.socket()
sk.bind=((modbus_ip,502))
sk.listen()
conn,addr=sk.accept()
print("连接成功")
while 1:
    try:
        from_client_data=conn.recv(1024)
        if from_client_data.upper()=="q":
            print("退出")
            break
        to_client_data="1234"
        sk.send(to_client_data)

    except ConnectionResetError:
        print("中断")
        break
conn.close()
sk.close()
#LOGGER.info(MASTER.execute(1,cst.READ_HOLDING_REGISTERS,0,4)) #an integer is required
