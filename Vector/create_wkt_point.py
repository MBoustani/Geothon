#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_point.py
Description:   This code create a wkt 3D point from latitude, longitue and elevation.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitude = 50
longitude = 100
#to make it 2D point
elevation = 0

point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(longitude, latitude, elevation)
point.ExportToWkt()
print point