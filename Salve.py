import sys
import time
import logging
import threading
import modbus_tk 
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import random

def main():
    LOGGER=modbus_tk.utils.create_logger(name="console",record_format="%(message)s")
    # creat server
    try:
        SERVER=modbus_tcp.TcpServer(address="192.168.1.111",port=502) #server error: [Errno 10049] The requested address is not valid in its context
        LOGGER.info("running...")
        LOGGER.info("enter'quit'for closing the server") 
        SERVER.start()
     # creat slave
        SERVE1=SERVER.add_slave(1)
        SERVE1.add_block('A',cst.HOLDING_REGISTERS,0,4)   

    finally:
        SERVER.stop()

if __name__=="__main__":
    main()