#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_point.py
Description:   This code creates a wkt point from longitue and latitude.
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

#define a point geometry
point = ogr.Geometry(ogr.wkbPoint)
#add point into point geometry
point.AddPoint(longitude, latitude, elevation)
#export point geometry into WKT format
point.ExportToWkt()
print point