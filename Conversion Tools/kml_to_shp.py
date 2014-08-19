#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/kml_to_shp.py
Description:   This code converts kml data format to shapefile format.
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

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#a kml example file
kml_file = "../static_files/kml/Google_Campus.kmz"

#set driver to ESRI shapefile to be able to create shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')

#output shapefile file name
shp_file = 'shapefile.shp'
#output shapefile layer name
layer_name = 'shapefile_layer'

#create shapefile data_source(file)
if os.path.exists(shp_file):
    driver.DeleteDataSource(shp_file)
shp_datasource = driver.CreateDataSource(shp_file)

#create a layer for shapefile
shp_layer = shp_datasource.CreateLayer(layer_name, srs, ogr.wkbPolygon)

#open KML file
kml_datasource = ogr.Open(kml_file)

#get number of layers in kml file
layer_number = kml_datasource.GetLayerCount()
for each in range(layer_number):
    #get each KML layer
    layer = kml_datasource.GetLayerByIndex(each)
    #get number of features from kml layer
    featurs_number = layer.GetFeatureCount()
    for i in range(featurs_number):
        #get each KML feature
        kml_feature = layer.GetFeature(i + 1)
        #get KML feature geometry
        feature_geometry = kml_feature.GetGeometryRef()

        #define a shapefile geometry
        shp_feature = ogr.Feature(shp_layer.GetLayerDefn())

        #set shapefile's feature geometry from KML's feature geometry
        shp_feature.SetGeometry(feature_geometry)

        #create shapefile's feature in shapefile's layer
        shp_layer.CreateFeature(shp_feature)

