#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_geojson_line.py
Description:   This code creates a geojson line file from some points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [30, 30, 40]
longitudes = [10, 20, 30]

line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(latitudes[0], longitudes[0])
line.AddPoint(latitudes[1], longitudes[1])
line.AddPoint(latitudes[2], longitudes[2])
geojson_line = line.ExportToJson()
print geojson_line
