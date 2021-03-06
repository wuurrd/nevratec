import os
import sys, urllib2
from xml.etree.ElementTree import fromstring
from math import *
from datetime import date
import csv
import urllib

def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, skipinitialspace=True):
        if line:
            yield line

def binary_search(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return lo

#read input arguments

class GPSError(Exception):
    pass

def query(address):
    address = str(address.decode('utf-8'))
    print 'address:',address
    page = "http://nominatim.openstreetmap.org/search?"
    page += urllib.urlencode(dict(q=address, format='xml', polygon=1))
    #fetch html source for page

    try:
        html = urllib2.urlopen(page).read()
    except:
        raise GPSError("ERROR: building not in database")

    ###get gps coordinates from polygonpoints
    #print html
    try:
        coords_list = fromstring(html).find('place').get("polygonpoints").lstrip('[[').rstrip(']]').split('],[')
    except:
        raise GPSError('Error finding polygon points for %s' % address)
    coords_gps = []

    for c in coords_list:
        tmp = c.lstrip('"').rstrip('"').split('","')
        entry = [float(tmp[0]),float(tmp[1])]
        coords_gps.append(entry)

    ###compute area from bounding polygon

    a_major = 6378137.0
    b_minor = 6356752.314245

    phi = coords_gps[0][0] * (2*pi / 360);

    R_loc = sqrt(
        ((a_major * a_major * cos(phi))**2 + (b_minor * b_minor * sin(phi))**2 )
        /
        ((a_major * cos(phi))**2 + (b_minor * sin(phi))**2)
        )

    #print "radius at location:", int(R_loc/1e03), "km"

    num_coords = len(coords_gps)

    #assert(num_coords >= 4)

    coords_cartesian = []

    coords_cartesian.append([0.0,0.0])

    #latitude, longitude <--> [0|1]

    for i in range(1,num_coords):

        dlon = (pi/180) * (coords_gps[i][1] - coords_gps[0][1])

        a_x = cos((pi/180) * coords_gps[i][0]) * cos((pi/180) * coords_gps[0][0]) * (sin(dlon/2))**2

        c_x = 2 * atan2(sqrt(a_x),sqrt(1-a_x))

        coord_x = R_loc * c_x;

        if coords_gps[i][1] < coords_gps[0][1]:
            coord_x *= -1

        ###

        dlat = (pi/180) * (coords_gps[i][0] - coords_gps[0][0])

        a_y = (sin(dlat/2))**2

        c_y = 2 * atan2(sqrt(a_y),sqrt(1-a_y))

        coord_y = R_loc * c_y

        if coords_gps[i][0] < coords_gps[0][0]:
            coord_y *= -1

        ###

        coords_cartesian.append([coord_x,coord_y])


    area = 0.0

    for i in range(num_coords-1):
        area += coords_cartesian[i][0] * coords_cartesian[i+1][1] - coords_cartesian[i+1][0] * coords_cartesian[i][1]

    area = 0.5 * abs(area)

    return area

    print "building area:", int(area), "m2"

    #current month

    month = date.today().strftime("%m").lstrip('0')

    print "current month:", month

    #optimal inclination angle - fetch from database

    #sun irrandiance per m2 at optimal inclination angle - fetch from database

    #installation price

    #electricity price

    #cumulative energy vs. time from area and sun intensity data. t=0 -->p
    #-(cost of installation)

    #cumulative energy costs saved vs. time from area and local t=0 --> 0
    #price data

if __name__ == '__main__':
    print query(' '.join(sys.argv))
