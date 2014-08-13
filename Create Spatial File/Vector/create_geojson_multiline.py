#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_geojson_multiline.py
Description:   This code creates a geojson multiline file from couple lines data.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [30, 30, 30]
longitudes = [10, 20, 30]

#define a multiline geometry
multiline = ogr.Geometry(ogr.wkbMultiLineString)

#add points to geometry
for i in range(len(latitudes)):
    line = ogr.Geometry(ogr.wkbLineString)
    line.AddPoint(longitudes[i], latitudes[i])
    multiline.AddGeometry(line)

#convert the multiline geometry to GeoJSON
geojson_multiline = multiline.ExportToJson()
print geojson_multiline
