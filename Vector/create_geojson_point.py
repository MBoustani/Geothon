#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_geojson_point.py
Description:   This code creates a geojson point file from latitude and longitude.
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
#in geojson longitude is first and then latitude
point.AddPoint(longitude, latitude)
geojson_point = point.ExportToJson()
print geojson_point
