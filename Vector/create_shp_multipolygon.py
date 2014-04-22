#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_multipolygon.py
Description:   This code create a multi polygon shapefile from some polygons.
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

latitudes = [10, 20, 30]
longitudes = [10, 40, 60]
shapefile = 'multipolygons.shp'
layer_name = 'multipolygon_layer'

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
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbMultiPolygon)

#create "Name" column for attribute table and set type as string
field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

#create first polygon
linear_ring_1 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_1.AddPoint(latitudes[0], longitudes[0])
linear_ring_1.AddPoint(latitudes[0], longitudes[1])
linear_ring_1.AddPoint(latitudes[1], longitudes[1])
linear_ring_1.AddPoint(latitudes[0], longitudes[0])
polygon_1 = ogr.Geometry(ogr.wkbPolygon)
polygon_1.AddGeometry(linear_ring_1)

#create a feature
feature = ogr.Feature(layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(polygon_1)

#add field "Name" to feature
feature.SetField("Name", 'polygon_1')

#create feature in layer
layer.CreateFeature(feature)

#create second polygon
linear_ring_2 = ogr.Geometry(ogr.wkbLinearRing)
linear_ring_2.AddPoint(latitudes[1], longitudes[1])
linear_ring_2.AddPoint(latitudes[1], longitudes[2])
linear_ring_2.AddPoint(latitudes[2], longitudes[2])
linear_ring_2.AddPoint(latitudes[1], longitudes[1])
polygon_2 = ogr.Geometry(ogr.wkbPolygon)
polygon_2.AddGeometry(linear_ring_2)

#create a feature
feature = ogr.Feature(layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(polygon_2)

#add field "Name" to feature
feature.SetField("Name", 'polygon_2')

#create feature in layer
layer.CreateFeature(feature)
