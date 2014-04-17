#!/usr/bin/env python

#Project:       Geothon (https://github.com/MBoustani/Geothon)
#File:          Vector/create_wkt_line.py
#Description:   This code create a wkt line from multi-points.
#Author:        Maziyar Boustani (github.com/MBoustani)

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes =  [50, 51, 52, 53, 54]
longitudes = [100, 110, 120, 130, 140]
#to make it 2D point
elevation = 0

line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(latitudes[0], longitudes[0], elevation)
line.AddPoint(latitudes[1], longitudes[1], elevation)
line.AddPoint(latitudes[2], longitudes[2], elevation)
line.AddPoint(latitudes[3], longitudes[3], elevation)
line.AddPoint(latitudes[4], longitudes[4], elevation)
line.ExportToWkt()
print line
