# Author:Zhengyu Sun
#Date: 03/05/2017
#This program is used for reading data frame in API mode from Xbee and writing data into a file.

import serial
import time
import datetime

#change value into hex
def hexShow(argv):
    result=''
    hLen=len(argv)
    for i in xrange(hLen):
        hvol=ord(argv[i])
        hhex='%02x'%hvol
        result+=hhex
    return result

 #open the recieving serial
ser=serial.Serial('COM4',38400)
str=ser.read(1)
while str!='':
    str=ser.read(1)
    data=hexShow(str)
    file = open('G:\pycharm_workspace\data.txt', 'a')
    if data=='7e':
        data=ser.read(2)
        data2=hexShow(data)
        value=int(data2,16)
        data=ser.read(1)
        data=ser.read(8)
        source=hexShow(data)
        data=ser.read(7)

        # get the data frame
        data=ser.read(value-16)
        print data

        # get date and recieving time
        date = time.strftime("%m/%d/%Y")
        time2 = time.strftime("%H:%M:%S")

        #write data,date and time to the file
        file.write(' Recieved:'+data+"\n")
        file.write('Date' + date +'   Time:'+time2+'\n')
        file.write('\n')

    #close the file
        file.close()

    #close the serial
ser.close()

