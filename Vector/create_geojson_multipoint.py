#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_geojson_multipoint.py
Description:   This code creates a geojson multipoint file from couple point data.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [30, 30, 30]
longitudes = [10, 20, 30]

#define multipoint geometry
multipoint = ogr.Geometry(ogr.wkbMultiPoint)

#create point geometry and add to multipoint geometry
for i in range(len(latitudes)):
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(longitudes[i], latitudes[i])
    multipoint.AddGeometry(point)

#convert geometry to GeoJSON format
geojson_multipoint = multipoint.ExportToJson()
print geojson_multipoint
