
import imp
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

def main():
    LOGGER=modbus_tk.utils.create_logger(name="console",record_format="%(message)s")
    # creat server
    try:
        SERVER=modbus_tcp.TcpServer(address="0.0.0.0",port=502) #server error: [Errno 10049] The requested address is not valid in its context
        LOGGER.info("running...")
        LOGGER.info("enter'quit'for closing the server") 
        SERVER.start()
     # creat slave
        SLAVE1=SERVER.add_slave(1)
        SLAVE1.add_block('A',cst.HOLDING_REGISTERS,0,2000) 
        #获取excel的数据   设置在寄存器 
        SLAVE1.set_values('A',0,getdata())
       

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
    data=table.cell(1,1).value
    print(data)
    #数据切片 TX count:0X3726==>0X3726
    cut_data=data[9:]
    print(cut_data)
    #数据转换 十六进制转化成十进制
    cut_data_10=str(int(hex(cut_data).upper(),16))
    
    print(cut_data_10)
    return cut_data

if __name__=="__main__":
    main()