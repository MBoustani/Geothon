#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_kml_point.py
Description:   This code creates a point kml from latitude and longitue.
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

latitude = 30
longitude = 10
kml = 'point.kml'
layer_name = 'point_layer'

#create KML dirver
driver = ogr.GetDriverByName('KML')

#create kml data_source(file)
data_source = driver.CreateDataSource(kml)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#create kml layer as point data with wgs84 as spatial reference
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbPoint)

#create "Name" column for attribute table and set type as string
field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

#create point geometry
point = ogr.Geometry(ogr.wkbPoint)

#add point into point geometry
point.AddPoint(longitude, latitude)

#create a feature
feature = ogr.Feature(layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(point)

#add field "Name" to feature
feature.SetField("Name", 'point_one')

#create feature in layer
layer.CreateFeature(feature)
