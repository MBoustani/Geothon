#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_multipolygon.py
Description:   This code create a wkt multi polygons from polygons
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [50, 51, 52, 53, 54, 55, 56, 57, 58]
longitudes = [100, 110, 120, 130, 140, 150, 160, 170, 180]
elevation = 0

multi_polygons = ogr.Geometry(ogr.wkbMultiPolygon)

linear_ring_1 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_1.AddPoint(longitudes[0], latitudes[0], elevation)
linear_ring_1.AddPoint(longitudes[1], latitudes[1], elevation)
linear_ring_1.AddPoint(longitudes[2], latitudes[2], elevation)
linear_ring_1.AddPoint(longitudes[0], latitudes[0], elevation)
polygon_1 = ogr.Geometry(ogr.wkbPolygon)
polygon_1.AddGeometry(linear_ring_1)
multi_polygons.AddGeometry(polygon_1)

linear_ring_2 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_2.AddPoint(longitudes[3], latitudes[3], elevation)
linear_ring_2.AddPoint(longitudes[4], latitudes[4], elevation)
linear_ring_2.AddPoint(longitudes[5], latitudes[5], elevation)
linear_ring_2.AddPoint(longitudes[3], latitudes[3], elevation)
polygon_2 = ogr.Geometry(ogr.wkbPolygon)
polygon_2.AddGeometry(linear_ring_2)
multi_polygons.AddGeometry(polygon_2)

linear_ring_3 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_3.AddPoint(longitudes[6], latitudes[6], elevation)
linear_ring_3.AddPoint(longitudes[7], latitudes[7], elevation)
linear_ring_3.AddPoint(longitudes[8], latitudes[8], elevation)
linear_ring_3.AddPoint(longitudes[6], latitudes[6], elevation)
polygon_3 = ogr.Geometry(ogr.wkbPolygon)
polygon_3.AddGeometry(linear_ring_3)
multi_polygons.AddGeometry(polygon_3)

multi_polygons.ExportToWkb()
print multi_polygons
