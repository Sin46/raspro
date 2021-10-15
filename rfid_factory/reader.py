import serial
import time
import binascii

ser = serial.Serial("/dev/ttyUSB0",115200)
print(ser.portstr)
test_data_1 = b'CC 09 03 00 01 CA 7A 07 70'
test_data_2 = b'CC 09 03 00 01 E6 EF 07 C9'
test_data_3 = b'CC 09 04 00 01 E7 2D 07 0D'

aaa = bytes.fromhex("cc0903000310f10723")
print(aaa.hex())

while True:
    data = ser.read(1).hex()
    if data=='cc':
        data = ser.read(1).hex()
        if data=='09':
            data = ser.read(7).hex()
            print(data[1])
        else:
            data_bytes = ser.read(6)   # <class 'bytes'>
            data_hex = data_bytes.hex()# <class 'str'>
            print('cc09'+data_hex)
            count = 0
            for temp in data_bytes[2:]:
                count = count+temp
            # print(count)
            
        # time.sleep(1)
        # print(time.time())
        # if(temp!=data[4]):
        #     print(time.time())
        #     temp=data[4]


    
    
