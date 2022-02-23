import sys
import logging
import modbus_tk 
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

modbus_ip="192.168.10.68"
Modbus_port="502"

LOGGER=modbus_tk.utils.create_logger("console")
MASTER=modbus_tcp.TcpMaster(host=modbus_ip,port=Modbus_port)
MASTER.set_timeout(5.0)
LOGGER.info("connected")

LOGGER.info(MASTER.execute(1,cst.READ_HOLDING_REGISTERS,0,4))
