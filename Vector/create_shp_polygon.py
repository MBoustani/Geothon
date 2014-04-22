#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_polygon.py
Description:   This code create a polygon shapefile from multi points.
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
shapefile = 'polygon.shp'
layer_name = 'polygon_layer'

#create ESRI shapefile dirver
driver = ogr.GetDriverByName('ESRI Shapefile')

#create shapefile data_source(file)
if os.path.exists(shapefile):
    driver.DeleteDataSource(shapefile)
data_source = driver.CreateDataSource(shapefile)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#create shapefile layer as polygon data with wgs84 as spatial reference
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbPolygon)

#create "Name" column for attribute table and set type as string
field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

#create polygon geometry
linear_ring = ogr.Geometry(ogr.wkbLinearRing)
linear_ring.AddPoint(latitudes[0], longitudes[0])
linear_ring.AddPoint(latitudes[1], longitudes[1])
linear_ring.AddPoint(latitudes[2], longitudes[2])
linear_ring.AddPoint(latitudes[3], longitudes[3])
linear_ring.AddPoint(latitudes[4], longitudes[4])
#last point should be first point to close polygon
linear_ring.AddPoint(latitudes[0], longitudes[0])
polygon = ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(linear_ring)

#create a feature
feature = ogr.Feature(layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(polygon)

#add field "Name" to feature
feature.SetField("Name", 'polygon_one')

#create feature in layer
layer.CreateFeature(feature)

