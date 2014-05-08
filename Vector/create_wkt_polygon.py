#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_polygon.py
Description:   This code create a wkt polygon from multi-points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [0, 10, 20, 30, 40]
longitudes = [0, 40, 50, 60, 40]
elevation = 0

#Create a linear rign from series of points
linear_ring = ogr.Geometry(ogr.wkbLinearRing)
linear_ring.AddPoint(longitudes[0], latitudes[0], elevation)
linear_ring.AddPoint(longitudes[1], latitudes[1], elevation)
linear_ring.AddPoint(longitudes[2], latitudes[2], elevation)
linear_ring.AddPoint(longitudes[3], latitudes[3], elevation)
#last point should be same as first point to close the ring
linear_ring.AddPoint(longitudes[4], latitudes[4], elevation)

#Create the polygon from linear ring
polygon = ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(linear_ring)
print polygon