import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)     #pin 23 als input van PIR motion sensor
pir_pin = 14


class Geluid(Thread):
    def __init__(self, mysqlcon):
        Thread.__init__(self)
        self.daemon = True
        self.conn = mysqlcon

        self.sensor_ID_geluid = self.conn.get_data('select * from  sensoren where naam_sensor="geluid"')
        if not self.sensor_ID_geluid:
            self.sensor_ID_geluid = self.conn.set_data('insert into sensoren values (2,"geluid",NULL,NULL )')
        else:
            self.sensor_ID_geluid = int(self.sensor_ID_geluid[0]['idsensor'])


        self.start()

    def run(self):
        while True:
            read_input = GPIO.input(pir_pin)
            if read_input == 1:
                print(read_input)
                self.conn.set_data('INSERT INTO metingen VALUES(NULL,%s, NOW(),%s)',[2, read_input])
                time.sleep(1)
