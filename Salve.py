import sys
import time
import logging
import threading
import modbus_tk 
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import random
import xlwt
import xlrd
import socket

def main():
    LOGGER=modbus_tk.utils.create_logger(name="console",record_format="%(message)s")
    # creat server
    try:
        SERVER=modbus_tcp.TcpServer(address="0.0.0.0",port=502) #server error: [Errno 10049] The requested address is not valid in its context
        LOGGER.info("running...")
        LOGGER.info("enter'quit'for closing the server") 
        SERVER.start()
        sk=socket.socket()
        sk.connect("0.0.0.0",502)

     # creat slave
        # SLAVE1=SERVER.add_slave(1)
        # SLAVE1.add_block('A',cst.HOLDING_REGISTERS,0,2000) 
        # #获取excel的数据   设置在寄存器 
        # SLAVE1.set_values('A',0,getdata())
       

        while True:
            CMD=sys.stdin.readline()
            if CMD.find('quit')==0:
                sys.stdout.write("system out")
                break
            else:
                sys.stdout.write("unknow command\n")

    finally:
        SERVER.stop()

#获取excel的数据
def getdata():
    xl=xlrd.open_workbook(r'Master_values.xlsx')
    table=xl.sheets()[0]
    #获取excel数据 TX count:0x3726
    data=table.cell(1,1).value
    print(data)
    #数据切片 TX count:0x3726==>0x3726
    cut_data=data[9:]
    print(cut_data)
    #数据转换 十六进制转化成十进制
    cut_data_10=(int(cut_data,16))
    print(cut_data_10)
    #获取excel数据 59 32 07 48
    data_01=table.cell(1,2).value
    print(data_01)
    #data_01_change= bytes().fromhex(int(data_01)) # python 3.0
    # for i in data_01:
    #     print("0x"+i)
    
    # print(data_01_change)
    
    return cut_data

if __name__=="__main__":
    main()