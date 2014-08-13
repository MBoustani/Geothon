#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Vector/create_shp_multipoint.py
Description:   This code creates points shapefile from some latitudes and longitues.
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

latitudes = [30, 30, 30]
longitudes = [10, 20, 30]
shapefile = 'multipoints.shp'
layer_name = 'multipoint_layer'

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

#create shapefile layer as points data with wgs84 as spatial reference
layer = data_source.CreateLayer(layer_name, srs, ogr.wkbPoint)

#create "Name" column for attribute table and set type as string
field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

for i in range(len(latitudes)):
    #define a point geometry
    point = ogr.Geometry(ogr.wkbPoint)

    #add point to the geometry
    point.AddPoint(longitudes[i], latitudes[i])

    #create a feature
    feature = ogr.Feature(layer.GetLayerDefn())

    #set point geometry to feature
    feature.SetGeometry(point)

    #add field "Name" to feature
    feature.SetField("Name", 'point_{0}'.format(str(i)))

    #create feature in layer
    layer.CreateFeature(feature)

    #destroy feature
    feature.Destroy()

