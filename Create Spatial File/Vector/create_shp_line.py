#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_line.py
Description:   This code create a line shapefile from multi-points.
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

latitudes = [30, 10, 40]
longitudes = [10, 20, 30]
shapefile = 'line.shp'
layer_name = 'line_layer'

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

#create shapefile layer as line data with wgs84 as spatial reference
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbLineString)

#create "Name" column for attribute table and set type as string
field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

#define line geometry
line = ogr.Geometry(ogr.wkbLineString)
#add points into line geometry
line.AddPoint(longitudes[0], latitudes[0])
line.AddPoint(longitudes[1], latitudes[1])
line.AddPoint(longitudes[2], latitudes[1])

#create a feature
feature = ogr.Feature(layer.GetLayerDefn())

#set feature geometry
feature.SetGeometry(line)

#add field "Name" to feature
feature.SetField("Name", 'line_one')

#create feature in layer
layer.CreateFeature(feature)
