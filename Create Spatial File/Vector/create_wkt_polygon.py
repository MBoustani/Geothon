#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_polygon.py
Description:   This code creates a wkt polygon from multi-points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [0, 10, 20, 30, 40]
longitudes = [0, 40, 50, 60, 40]
elevation = 0

#define linear ring geometry
linear_ring = ogr.Geometry(ogr.wkbLinearRing)
#add points into linear geometry
linear_ring.AddPoint(longitudes[0], latitudes[0], elevation)
linear_ring.AddPoint(longitudes[1], latitudes[1], elevation)
linear_ring.AddPoint(longitudes[2], latitudes[2], elevation)
linear_ring.AddPoint(longitudes[3], latitudes[3], elevation)
#last point should be same as first point to close the ring
linear_ring.AddPoint(longitudes[4], latitudes[4], elevation)
#define polygon geometry
polygon = ogr.Geometry(ogr.wkbPolygon)
#add linear geometry into polygon geometry
polygon.AddGeometry(linear_ring)
#export polygon geometry into WKT format
polygon.ExportToWkt()
print polygon