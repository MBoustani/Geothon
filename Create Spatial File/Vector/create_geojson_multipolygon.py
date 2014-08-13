#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_geojson_multipolygon.py
Description:   This code creates a multipolygon geojson file from some points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [10, 20, 30]
longitudes = [10, 40, 60]

#define multipolygon geometry
multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)

#create first polygon
#create first linear ring
linear_ring_1 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_1.AddPoint(longitudes[0], latitudes[0])
linear_ring_1.AddPoint(longitudes[1], latitudes[0])
linear_ring_1.AddPoint(longitudes[1], latitudes[1])
linear_ring_1.AddPoint(longitudes[0], latitudes[0])
#define polygon geometry
polygon_1 = ogr.Geometry(ogr.wkbPolygon)
#add linear ring to polygon geometry
polygon_1.AddGeometry(linear_ring_1)
#add polygon to multipolygon geometry
multipolygon.AddGeometry(polygon_1)

#create second polygon
#create second linear ring
linear_ring_2 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_2.AddPoint(longitudes[1], latitudes[1])
linear_ring_2.AddPoint(longitudes[2], latitudes[1])
linear_ring_2.AddPoint(longitudes[2], latitudes[2])
linear_ring_2.AddPoint(longitudes[1], latitudes[1])
#define polygon geometry
polygon_2 = ogr.Geometry(ogr.wkbPolygon)
#add linear ring to polygon geometry
polygon_2.AddGeometry(linear_ring_2)
#add polygon to multipolygon geometry
multipolygon.AddGeometry(polygon_2)

#convert multipolygon geometry to GeoJSON format
geojson_multipolygon = multipolygon.ExportToJson()
print geojson_multipolygon
