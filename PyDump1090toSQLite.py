import socket
import collections
import json
import sqlite3

dbname = '/home/pi/dump.db'

# store messge in the local database
def log_message(msg, hex, sqwk, flight, alt, lat, lon, date, time):
        print 'data: ' + msg, hex, sqwk, flight, alt, lat, lon, date, time

        conn = sqlite3.connect(dbname)
        curs = conn.cursor()

        curs.execute("INSERT INTO adsb_messages values(datetime('now'), (?), (?), (?), (?), (?), (?), (?), (?), (?))", (msg, hex, sqwk, flight, alt, lat, lon, date, time))

        # commit the changes
        conn.commit()

        # display last

        conn.close()

def display_data():

        conn = sqlite3.connect(dbname)
        curs = conn.cursor()

        for row in curs.execute("SELECT MAX(timestamp), msg, hex, sqwk, flight, alt, lat, lon, date, time FROM adsb_messages"):
                print row

        conn.close()

print "Program started."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 30003))
while True:
        output = s.recv(1024)
        print output
        output2 = output.split(",")
        if output2[1] == '3' or output2[1] == '6' or output2[1] == '5' or output2[1] == '7':
                msg = output2[1]
                hexident = output2[4]
                sqwk = output2[19]
                flight = output2[10]
                alt = output2[11]
                lat = output2[14]
                lon = output2[15]
                date = output2[6]
                time = output2[7]

                log_message(msg, hexident, sqwk, flight, alt, lat, lon, date, time)

                display_data()
