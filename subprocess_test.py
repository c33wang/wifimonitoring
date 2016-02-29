import subprocess
import time
from apscheduler.schedulers.blocking import BlockingScheduler

import json
import bottle
from bottle import route, run, request, abort
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
import re


connection = MongoClient('localhost', 27017)
db2 = connection.yourdatabase



sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=1)

def timed_job():

    now = time.strftime("%c")
    data = subprocess.check_output(["iwconfig", "wlan0"])
    data_line = data.split('\n')

    Bit_rate = data_line[2]
    bitRateTx = re.split('=| \s+', data_line[2])
    bitRate = bitRateTx[2]
    Tx = bitRateTx[4]

    data5 = re.split('=| \s+', data_line[5])
    SignalLevel = data5[4]


    print time.strftime("%c")
    print bitRate
    print Tx
    print SignalLevel


    ping = subprocess.check_output("ping 192.168.1.1 -c 10 -I wlan0", shell = True)
    print ping

    insert_sample_data = db2.wifi.insert_one({"Bit Rate": bitRate, "Tx": Tx, "SignalLevel": SignalLevel})



sched.start()




