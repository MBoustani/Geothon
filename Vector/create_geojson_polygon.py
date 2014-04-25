#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_geojson_polygon.py
Description:   This code creates a geojson polygon file from some points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [0, 10, 20, 30, 40]
longitudes = [0, 40, 50, 60, 40]

#define polygon geometry
polygon = ogr.Geometry(ogr.wkbPolygon)

linear_ring = ogr.Geometry(ogr.wkbLinearRing)
linear_ring.AddPoint(latitudes[0], longitudes[0])
linear_ring.AddPoint(latitudes[1], longitudes[1])
linear_ring.AddPoint(latitudes[2], longitudes[2])
linear_ring.AddPoint(latitudes[3], longitudes[3])
linear_ring.AddPoint(latitudes[4], longitudes[4])
#last point should be first point to close polygon
linear_ring.AddPoint(latitudes[0], longitudes[0])

#add linear ring to polygon geometry
polygon.AddGeometry(linear_ring)

#export geometry to GeoJSON
geojson_polygon = polygon.ExportToJson()
print geojson_polygon
