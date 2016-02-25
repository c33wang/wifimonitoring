Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from bottle
SyntaxError: invalid syntax
>>> from pymongo import MongoClient
>>> connection = MongoClient()
>>> db2 = connection.yourdatabase
>>> db2.find_one()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    db2.find_one()
  File "/usr/local/lib/python2.7/dist-packages/pymongo/collection.py", line 2343, in __call__
    self.__name)
TypeError: 'Collection' object is not callable. If you meant to call the 'find_one' method on a 'Database' object it is failing because no such method exists.
>>> db2.find_one()

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    db2.find_one()
  File "/usr/local/lib/python2.7/dist-packages/pymongo/collection.py", line 2343, in __call__
    self.__name)
TypeError: 'Collection' object is not callable. If you meant to call the 'find_one' method on a 'Database' object it is failing because no such method exists.
>>> db2 = connection.yourdatabase
>>> db2.find_one()

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    db2.find_one()
  File "/usr/local/lib/python2.7/dist-packages/pymongo/collection.py", line 2343, in __call__
    self.__name)
TypeError: 'Collection' object is not callable. If you meant to call the 'find_one' method on a 'Database' object it is failing because no such method exists.
>>> db2.wifi.find_one()
{u'_id': ObjectId('56cb435874fece0b37096a4d'), u'data': u'wlan0     IEEE 802.11bgn  ESSID:"2WIRE716"  \n          Mode:Managed  Frequency:2.462 GHz  Access Point: 44:D9:E7:03:00:A5   \n          Bit Rate=1 Mb/s   Tx-Power=20 dBm   \n          Retry short limit:7   RTS thr:off   Fragment thr:off\n          Power Management:off\n          Link Quality=70/70  Signal level=-17 dBm  \n          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0\n          Tx excessive retries:435  Invalid misc:175   Missed beacon:0\n\n'}
>>> db2.wifi.dump()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    db2.wifi.dump()
  File "/usr/local/lib/python2.7/dist-packages/pymongo/collection.py", line 2347, in __call__
    self.__name.split(".")[-1])
TypeError: 'Collection' object is not callable. If you meant to call the 'dump' method on a 'Collection' object it is failing because no such method exists.
>>> db2.wifi.drop()
>>> db2.wifi.find_one()
>>> db2.wifi.find_one()
{u'Bit Rate': u'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   ', u'_id': ObjectId('56ccdfea74fece05c35e25ab'), u'Link Quality': u'          Link Quality=70/70  Signal level=-39 dBm  '}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ifconfig

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ifconfig
NameError: name 'ifconfig' is not defined
>>> db2.wifi.dump()

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    db2.wifi.dump()
  File "/usr/local/lib/python2.7/dist-packages/pymongo/collection.py", line 2347, in __call__
    self.__name.split(".")[-1])
TypeError: 'Collection' object is not callable. If you meant to call the 'dump' method on a 'Collection' object it is failing because no such method exists.
>>> db2.wifi.dump
Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'yourdatabase'), u'wifi.dump')
>>> db2.wifi.drop()
>>> db2.wifi.drop()
>>> 
>>>     data = subprocess.check_output(["iwconfig", "wlan0"])

  File "<pyshell#24>", line 1
    data = subprocess.check_output(["iwconfig", "wlan0"])
    ^
IndentationError: unexpected indent
>>> data = subprocess.check_output(["iwconfig", "wlan0"])


Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data = subprocess.check_output(["iwconfig", "wlan0"])
NameError: name 'subprocess' is not defined
>>> import subprocess
>>> data = subprocess.check_output(["iwconfig", "wlan0"])
>>> data_line = data.split('\n')
>>> Bit_rate = data_line[2]
>>> Link_qual = data_line[5]
>>> from datetime import datetime
>>> now = time.strftime("%c")

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    now = time.strftime("%c")
NameError: name 'time' is not defined
>>> import time
>>> now = time.strftime("%c")
>>> now
'Wed Feb 24 22:11:05 2016'
>>> db2.wifi.drop()
>>> insert_sample_data = db2.wifi.insert_one({"Bit Rate":Bit_rate)
					 
SyntaxError: invalid syntax
>>> insert_sample_data = db2.wifi.insert_one({"Bit Rate":Bit_rate})
>>> insert_sample_data = db2.wifi.insert_one({Bit_rate})

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    insert_sample_data = db2.wifi.insert_one({Bit_rate})
  File "/usr/local/lib/python2.7/dist-packages/pymongo/collection.py", line 619, in insert_one
    common.validate_is_document_type("document", document)
  File "/usr/local/lib/python2.7/dist-packages/pymongo/common.py", line 384, in validate_is_document_type
    "collections.MutableMapping" % (option,))
TypeError: document must be an instance of dict, bson.son.SON, bson.raw_bson.RawBSONDocument, or a type that inherits from collections.MutableMapping
>>> insert_sample_data = db2.wifi.insert_one({now:Bit_rate})
>>> db2.wifi.drop()
>>> insert_sample_data = db2.wifi.insert_one({now:Bit_rate})
>>> insert_sample_data = db2.wifi.insert_one({now:Bit_rate, Link_qual})
SyntaxError: invalid syntax
>>> insert_sample_data = db2.wifi.insert_one({[now:Bit_rate, Link_qual]})
SyntaxError: invalid syntax
>>> 
>>> Bit_rate = data_line[2]
>>> Bit_rate
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> data_line[2][3]
' '
>>> data_line[2][6]
' '
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> equal = data_line[2].split('=')
>>> equal
['          Bit Rate', '1 Mb/s   Tx-Power', '20 dBm   ']
>>> print equal[1]
1 Mb/s   Tx-Power
>>> equal = data_line[2].split('= | s')
>>> equal
['          Bit Rate=1 Mb/s   Tx-Power=20 dBm   ']
>>> equal = data_line[2].split('=')
>>> equal
['          Bit Rate', '1 Mb/s   Tx-Power', '20 dBm   ']
>>> equal = data_line[2].split('=', 1 )
>>> equal
['          Bit Rate', '1 Mb/s   Tx-Power=20 dBm   ']
>>> equal = data_line[2].split('=', 1 )
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> equal = data_line[2].split('=', 1 )
>>> equal
['          Bit Rate', '1 Mb/s   Tx-Power=20 dBm   ']
>>> fequal = equal.split()

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    fequal = equal.split()
AttributeError: 'list' object has no attribute 'split'
>>> 
>>> 
>>> 
>>> 
>>> dat

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    dat
NameError: name 'dat' is not defined
>>> data
'wlan0     IEEE 802.11bgn  ESSID:"ctest_o"  \n          Mode:Managed  Frequency:2.462 GHz  Access Point: 44:D9:E7:FA:16:07   \n          Bit Rate=1 Mb/s   Tx-Power=20 dBm   \n          Retry short limit:7   RTS thr:off   Fragment thr:off\n          Power Management:off\n          Link Quality=70/70  Signal level=-39 dBm  \n          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0\n          Tx excessive retries:625  Invalid misc:2769   Missed beacon:0\n\n'
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> second = data_line[2].split('\s+')
>>> second
['          Bit Rate=1 Mb/s   Tx-Power=20 dBm   ']
>>> second[1]

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    second[1]
IndexError: list index out of range
>>> second = data_line[2].split('')

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    second = data_line[2].split('')
ValueError: empty separator
>>> second = data_line[2].split('   ')
>>> second
['', '', '', ' Bit Rate=1 Mb/s', 'Tx-Power=20 dBm', '']
>>> len(second)
6
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> import re
>>> data2 = re.split(', | \s+', data_line[2])
>>> data2
['', 'Bit Rate=1 Mb/s', 'Tx-Power=20 dBm', '']
>>> data2 = re.split('= | \s+', data_line[2])
>>> data2
['', 'Bit Rate=1 Mb/s', 'Tx-Power=20 dBm', '']
>>> data2 = re.split(' = | \s+', data_line[2])
>>> data2
['', 'Bit Rate=1 Mb/s', 'Tx-Power=20 dBm', '']
>>> data2 = re.split(' = ', data_line[2])
>>> data2
['          Bit Rate=1 Mb/s   Tx-Power=20 dBm   ']
>>> data[2]
'a'
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> data2
['          Bit Rate=1 Mb/s   Tx-Power=20 dBm   ']
>>> 
>>> 
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> data_line[1]
'          Mode:Managed  Frequency:2.462 GHz  Access Point: 44:D9:E7:FA:16:07   '
>>> data_line[2]
'          Bit Rate=1 Mb/s   Tx-Power=20 dBm   '
>>> data2 = re.split(', | \s+', data_line[2])
>>> data2
['', 'Bit Rate=1 Mb/s', 'Tx-Power=20 dBm', '']
>>> data2 = re.split('=', data_line[2])
>>> data2
['          Bit Rate', '1 Mb/s   Tx-Power', '20 dBm   ']
>>> data2 = re.split('=| \s+', data_line[2])
>>> data2
['', 'Bit Rate', '1 Mb/s', 'Tx-Power', '20 dBm', '']
>>> for a in data2:
	print a

	

Bit Rate
1 Mb/s
Tx-Power
20 dBm

>>> data2[0]
''
>>> data2[2]
'1 Mb/s'
>>> data2[3]
'Tx-Power'
>>> data2[4]
'20 dBm'
>>> data_line[5]
'          Link Quality=70/70  Signal level=-39 dBm  '
>>> data5 = re.split('=| \s+', data_line[5])
>>> 
>>> data5
['', 'Link Quality', '70/70', 'Signal level', '-39 dBm', '']
>>> data5[5]
''
>>> data5[4]
'-39 dBm'
>>> 
