import RPi.GPIO as GPIO
import time
from threading import Thread
from mcp import Mcp3008

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)     #pin 23 als input van PIR motion sensor
pir_pin = 23


class Gewicht(Thread):
    def __init__(self, mysqlcon):
        Thread.__init__(self)
        self.daemon = True
        self.conn = mysqlcon

        self.sensor_ID_gewicht = self.conn.get_data('SELECT * FROM sensoren WHERE naam_sensor="gewicht"')
        if not self.sensor_ID_gewicht:
            self.sensor_ID_gewicht = self.conn.set_data('INSERT INTO sensoren VALUES(3,"gewicht",NULL,NULL)')
        else:
            self.sensor_ID_gewicht = int(self.sensor_ID_gewicht[0]['idsensor'])


        self.start()

    def run(self):
        print("started")
        mcp = Mcp3008()
        while True:
            answer_druk = mcp.read_channel(0)
            answer_druk = answer_druk / 1.023
            if answer_druk > 500:
                print("gewicht")
                self.conn.set_data('INSERT INTO metingen VALUES(NULL,%s, NOW(),%s)', [self.sensor_ID_gewicht,answer_druk])
                time.sleep(5)


