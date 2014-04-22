#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_multiline.py
Description:   This code create a multiline shapefile from multi lines.
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

latitude = [30, 30, 40]
longitude = [10, 20, 30]
shapefile = 'multilines.shp'
layer_name = 'multilines_layer'

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

#list of lines geometry
lines = []

#create first line geometry
line_1 = ogr.Geometry(ogr.wkbLineString)
line_1.AddPoint(latitude[0], longitude[0])
line_1.AddPoint(latitude[1], longitude[1])
line_1.AddPoint(latitude[2], longitude[2])
lines.append(line_1)

#create second line geometry
line_2 = ogr.Geometry(ogr.wkbLineString)
line_2.AddPoint(latitude[1], longitude[0])
line_2.AddPoint(latitude[2], longitude[1])
line_2.AddPoint(latitude[1], longitude[2])
lines.append(line_2)

for i in range(len(lines)):
    #create a feature
    feature = ogr.Feature(layer.GetLayerDefn())

    #set feature geometry
    feature.SetGeometry(lines[i])

    #add field "Name" to feature
    feature.SetField("Name", 'line_{0}'.format(str(i)))

    #create feature in layer
    layer.CreateFeature(feature)
