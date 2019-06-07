import time
import requests
from opensky_api import OpenSkyApi

api = OpenSkyApi()
while True:
    s = api.get_states(bbox=(33.1951,33.3397,-111.8169,-111.6440))
    for s1 in s.states:
        print("(%r, %r, %r, %r, %r)" % \
               (s1.callsign, s1.longitude, s1.latitude,\
                s1.baro_altitude, s1.velocity))
    print("--------\n")
    time.sleep(30)
