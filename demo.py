import time
import requests
from opensky_api import OpenSkyApi

api = OpenSkyApi()
while True:
#	s = api.get_states(bbox=(33.1951,33.3397,-111.8169,-111.6440)) home
	s = api.get_states(bbox=(33.0004524786153, 33.8678875213847, -112.531391304461, -111.491948695539))
	for s1 in s.states:
		callsign = (s1.callsign + " "*8)[:7]
		f_altitude = float(s1.baro_altitude) * 3.2804
		t_altitude = "%6.1f" % f_altitude
		f_velocity = float(s1.velocity) * 2.23694
		t_velocity = "%4.1f" % f_velocity
		print("(%r, %r, %r, %r, %r)" % \
			(s1.callsign, s1.longitude, s1.latitude,\
			t_altitude, t_velocity))
	print("--------\n\n")
	time.sleep(30)