#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_multipolygon.py
Description:   This code creates a wkt multi polygons from some polygons
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [50, 60, 54, 53, 40, 55, 56, 37, 58]
longitudes = [100, 120, 145, 130, 120, 150, 160, 170, 180]
elevation = 0

#define a multi-polygon geometry
multi_polygons = ogr.Geometry(ogr.wkbMultiPolygon)

#create first polygon
#define first linear ring geometry
linear_ring_1 = ogr.Geometry(ogr.wkbLinearRing)
#add points into first linear ring geoemetry
linear_ring_1.AddPoint(longitudes[0], latitudes[0], elevation)
linear_ring_1.AddPoint(longitudes[1], latitudes[1], elevation)
linear_ring_1.AddPoint(longitudes[2], latitudes[2], elevation)
linear_ring_1.AddPoint(longitudes[0], latitudes[0], elevation)
#define first polygon geometry
polygon_1 = ogr.Geometry(ogr.wkbPolygon)
#add first linear ring into first polygon geometry
polygon_1.AddGeometry(linear_ring_1)
#add first polygon geometry into multi-polygon geometry
multi_polygons.AddGeometry(polygon_1)

#create second polygon
#define second linear ring geometry
linear_ring_2 = ogr.Geometry(ogr.wkbLinearRing)
#add points into second linear ring geoemetry
linear_ring_2.AddPoint(longitudes[3], latitudes[3], elevation)
linear_ring_2.AddPoint(longitudes[4], latitudes[4], elevation)
linear_ring_2.AddPoint(longitudes[5], latitudes[5], elevation)
linear_ring_2.AddPoint(longitudes[3], latitudes[3], elevation)
#define second polygon geometry
polygon_2 = ogr.Geometry(ogr.wkbPolygon)
#add second linear ring into second polygon geometry
polygon_2.AddGeometry(linear_ring_2)
#add second polygon geometry into multi-polygon geometry
multi_polygons.AddGeometry(polygon_2)

#create third polygon
#define third linear ring geometry
linear_ring_3 = ogr.Geometry(ogr.wkbLinearRing)
#add points into third linear ring geoemetry
linear_ring_3.AddPoint(longitudes[6], latitudes[6], elevation)
linear_ring_3.AddPoint(longitudes[7], latitudes[7], elevation)
linear_ring_3.AddPoint(longitudes[8], latitudes[8], elevation)
linear_ring_3.AddPoint(longitudes[6], latitudes[6], elevation)
#define third polygon geometry
polygon_3 = ogr.Geometry(ogr.wkbPolygon)
#add third linear ring into third polygon geometry
polygon_3.AddGeometry(linear_ring_3)
#add third polygon geometry into multi-polygon geometry
multi_polygons.AddGeometry(polygon_3)

#export multi-polygon geometry into WKT format
multi_polygons.ExportToWkb()
print multi_polygons
