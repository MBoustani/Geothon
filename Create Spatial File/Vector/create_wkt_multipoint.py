#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_wkt_multipoint.py
Description:   This code creates a wkt multi point from longitue and latitude.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

latitudes = [50, 51, 52, 53, 54]
longitudes = [100, 110, 120, 130, 140]
#to make 2D point
elevation = 0

#define multi-points geometry
points = ogr.Geometry(ogr.wkbMultiPoint)

#make first point
#define first point geometry
point_1 = ogr.Geometry(ogr.wkbPoint)
#add point into first point geometry
point_1.AddPoint(longitudes[0], latitudes[0], elevation)
#add first point geometry into multi-point geometry
points.AddGeometry(point_1)

#make second point
#define second point geometry
point_2 = ogr.Geometry(ogr.wkbPoint)
#add point into second point geometry
point_2.AddPoint(longitudes[1], latitudes[1], elevation)
#add second point geometry into multi-point geometry
points.AddGeometry(point_2)

#make third point
#define third point geometry
point_3 = ogr.Geometry(ogr.wkbPoint)
#add point into thirs point geometry
point_3.AddPoint(longitudes[2], latitudes[2], elevation)
#add third point geometry into multi-point geometry
points.AddGeometry(point_3)

#make fourth point
#define fourth point geometry
point_4 = ogr.Geometry(ogr.wkbPoint)
#add point into fourth point geometry
point_4.AddPoint(longitudes[3], latitudes[3], elevation)
#add fourth point geometry into multi-point geometry
points.AddGeometry(point_4)

#make fifth point
#define fifth point geometry
point_5 = ogr.Geometry(ogr.wkbPoint)
#add point into fifth point geometry
point_5.AddPoint(longitudes[4], latitudes[4], elevation)
#add fifth point geometry into multi-point geometry
points.AddGeometry(point_5)

#convert multi-point geometry into WKT format
points.ExportToWkt()
print points
