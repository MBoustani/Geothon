#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_line.py
Description:   This code creates a wkt line from multi-points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes =  [50, 51, 52, 53, 54]
longitudes = [100, 110, 120, 130, 140]
#to make it 2D point
elevation = 0

#define a line geometry
line = ogr.Geometry(ogr.wkbLineString)
#add points into line geometry
line.AddPoint(longitudes[0], latitudes[0], elevation)
line.AddPoint(longitudes[1], latitudes[1], elevation)
line.AddPoint(longitudes[2], latitudes[2], elevation)
line.AddPoint(longitudes[3], latitudes[3], elevation)
line.AddPoint(longitudes[4], latitudes[4], elevation)
#convert line geometry into WKT format
line.ExportToWkt()
print line
