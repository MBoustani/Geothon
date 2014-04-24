#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_multipoint.py
Description:   This code creates a wkt multi 3D point from latitude, longitue and elevation.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [50, 51, 52, 53, 54]
longitudes = [100, 110, 120, 130, 140]
elevation = 0   #to make 2D point

points = ogr.Geometry(ogr.wkbMultiPoint)


point_1 = ogr.Geometry(ogr.wkbPoint)
point_1.AddPoint(longitudes[0], latitudes[0], elevation)
points.AddGeometry(point_1)

point_2 = ogr.Geometry(ogr.wkbPoint)
point_2.AddPoint(longitudes[1], latitudes[1], elevation)
points.AddGeometry(point_2)

point_3 = ogr.Geometry(ogr.wkbPoint)
point_3.AddPoint(longitudes[2], latitudes[2], elevation)
points.AddGeometry(point_3)

point_4 = ogr.Geometry(ogr.wkbPoint)
point_4.AddPoint(longitudes[3], latitudes[3], elevation)
points.AddGeometry(point_4)

point_5 = ogr.Geometry(ogr.wkbPoint)
point_5.AddPoint(longitudes[4], latitudes[4], elevation)
points.AddGeometry(point_5)

points.ExportToWkt()
print points
