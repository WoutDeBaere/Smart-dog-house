from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS
from DP1Database import Database
import beweging
import geluid
import gewicht
from lcd import LCDScreen
from RPi import GPIO

app = Flask(__name__)

CORS(app)
conn = Database(app=app, user='wout', password='etdvvz', db='mydb')
lcd = LCDScreen(False, 21, 20, 13, 19, 26, 17, 24, 25, 12, 16)
lcd.LCD_init()

lcd.send_line('Smart dog house')
lcd.second_row()
lcd.statusip1()
lopen = beweging.Beweging(conn)
geluid = geluid.Geluid(conn)
gewicht = gewicht.Gewicht(conn)


socketio = SocketIO(app)


@socketio.on('getbeweging')
def beweging():
    bew = conn.get_data('SELECT count(*)*5 FROM metingen WHERE sensoren_idsensor = 1 and Date_time >= (CURRENT_DATE) AND Date_time < ((CURRENT_DATE ) + INTERVAL 1 DAY);')
    print(bew)
    socketio.emit('givebeweging', str(bew[0]['count(*)*5']))

@socketio.on('getgeluid')
def geluid():
    geluid = conn.get_data('SELECT count(*) FROM metingen WHERE sensoren_idsensor = 2 and Date_time >= (CURRENT_DATE) AND Date_time < ((CURRENT_DATE ) + INTERVAL 1 DAY);')
    socketio.emit('givegeluid', str(geluid[0]['count(*)']))

@socketio.on('getweight')
def gewicht():
    gewicht = conn.get_data('SELECT count(*)*5 FROM metingen WHERE sensoren_idsensor = 3 and Date_time >= (CURRENT_DATE) AND Date_time < ((CURRENT_DATE ) + INTERVAL 1 DAY) ;')
    socketio.emit('giveweight', str(gewicht[0]['count(*)*5']))

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port="5000")

