import time
import serial
import random

lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

while True:
    word_file = "words"
    WORDS = open(word_file).read().splitlines()
    final=random.choice(WORDS)
    b = bytes(final,'utf-8')
    s = lora.write(b)#send the data to other lora
    print (final)
    time.sleep(40)#delay of 40s
