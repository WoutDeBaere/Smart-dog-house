import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)     #pin 23 als input van PIR motion sensor
pir_pin = 23


class Beweging(Thread):
    def __init__(self, mysqlcon):
        Thread.__init__(self)
        self.daemon = True
        self.conn = mysqlcon

        self.sensor_ID_beweging = self.conn.get_data('SELECT * FROM sensoren WHERE naam_sensor="beweging"')
        if not self.sensor_ID_beweging:
            self.sensor_ID_beweging = self.conn.set_data('INSERT INTO sensoren VALUES(1,"beweging",NULL,NULL )')
        else:
            self.sensor_ID_beweging = int(self.sensor_ID_beweging[0]['idsensor'])

        self.start()

    def run(self):
        print("started")
        while True:
            read_input = GPIO.input(pir_pin)
            if read_input == 1:
                print("jaaaa")
                self.conn.set_data('INSERT INTO metingen VALUES(NULL,%s, NOW(),1)', [self.sensor_ID_beweging])
                time.sleep(5)
