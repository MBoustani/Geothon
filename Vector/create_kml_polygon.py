#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_kml_polygon.py
Description:   This code creates a polygon kml from multi-points.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr

latitudes = [0, 10, 20, 30, 40]
longitudes = [0, 40, 50, 60, 40]
kml = 'polygon.kml'
layer_name = 'polygon_layer'

#create KML dirver
driver = ogr.GetDriverByName('KML')

#create kml data_source(file)
data_source = driver.CreateDataSource(kml)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#create kml layer as polygon data with wgs84 as spatial reference
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbPolygon)

#create "Name" column for attribute table and set type as string
field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

#define linear ring geometry
linear_ring = ogr.Geometry(ogr.wkbLinearRing)
#add points into linear ring geometry
linear_ring.AddPoint(longitudes[0], latitudes[0])
linear_ring.AddPoint(longitudes[1], latitudes[1])
linear_ring.AddPoint(longitudes[2], latitudes[2])
linear_ring.AddPoint(longitudes[3], latitudes[3])
linear_ring.AddPoint(longitudes[4], latitudes[4])
#last point should be first point to close polygon
linear_ring.AddPoint(longitudes[0], latitudes[0])
#define polygon geometry
polygon = ogr.Geometry(ogr.wkbPolygon)
#add linear ring geometry into polygon geometry
polygon.AddGeometry(linear_ring)

#create a feature
feature = ogr.Feature(layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(polygon)

#add field "Name" to feature
feature.SetField("Name", 'polygon_one')

#create feature in layer
layer.CreateFeature(feature)
