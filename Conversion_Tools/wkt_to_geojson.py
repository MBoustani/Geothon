#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/wkt_to_geojson.py
Description:   This code converts wkt data format to geojson format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

#example WKT data in three geometry format
wkt_point = "POINT (102.0 0.6)"
wkt_line = "LINESTRING (102 0,103 1,104 0,105 1)"
wkt_polygon = "POLYGON ((100 0,101 0,101 1,100 1,100 0))"

#convert WKT format to geometry format
point_geometry = ogr.CreateGeometryFromWkt(wkt_point)
print point_geometry.ExportToJson()

#convert WKT format to geometry format
line_geometry = ogr.CreateGeometryFromWkt(wkt_line)
print line_geometry.ExportToJson()

#convert WKT format to geometry format
polygon_geometry = ogr.CreateGeometryFromWkt(wkt_polygon)
print polygon_geometry.ExportToJson()
