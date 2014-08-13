#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_multiline.py
Description:   This code creates a multiline shapefile from multi-lines.
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

#define first line geometry
line_1 = ogr.Geometry(ogr.wkbLineString)
#add points into first line geometry
line_1.AddPoint(longitude[0], latitude[0])
line_1.AddPoint(longitude[1], latitude[1])
line_1.AddPoint(longitude[2], latitude[2])
lines.append(line_1)

#define second line geometry
line_2 = ogr.Geometry(ogr.wkbLineString)
#add points into second line geometry
line_2.AddPoint(longitude[0], latitude[1])
line_2.AddPoint(longitude[1], latitude[2])
line_2.AddPoint(longitude[2], latitude[1])
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
