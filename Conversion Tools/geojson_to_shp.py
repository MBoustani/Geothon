#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/geojson_to_shp.py
Description:   This code converts geojson data format to shapefile format.
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

#set driver to ESRI shapefile to be able to create shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')

#this GeoJSON file has all three types of geometry (point, line and polygon)
json_file = "../static_files/geojson/test.json"

#open the GeoJSON file
geojson_datasource = ogr.Open(json_file)

#get GeoJSON layers number
geojson_layer_number = geojson_datasource.GetLayerCount()

for layer in range(geojson_layer_number):
    #get GeoJSON one layer
    geojson_layer = geojson_datasource.GetLayerByIndex(layer)
    #get number of features from GeoJSON's layer
    geojson_feature_number = geojson_layer.GetFeatureCount()
    for feature in range(geojson_feature_number):
        #get feature from GeoJSON's layer
        geojson_feature = geojson_layer.GetFeature(feature)
        #get feature's geometry
        geojson_feature_geom = geojson_feature.GetGeometryRef()
        #get feature's geometry type
        geojson_feature_type = geojson_feature_geom.GetGeometryType()
        #get feature's geometry type as name
        geojson_feature_name = geojson_feature_geom.GetGeometryName()

        #create a new shapefile for each geometry (point, line and polygon)
        shp_file = 'shapefile_{0}.shp'.format(geojson_feature_name)
        #define a layer for each shapefile
        layer_name = 'shapefile_layer'

        #create shapefile data_source(file)
        if os.path.exists(shp_file):
            driver.DeleteDataSource(shp_file)
        shp_datasource = driver.CreateDataSource(shp_file)

        #create a shapefile layer
        shp_layer = shp_datasource.CreateLayer(layer_name, srs, geojson_feature_type)

        #define a feature for shapefile
        feature = ogr.Feature(shp_layer.GetLayerDefn())
        #add geometry from GeoJSON to shapefile feature
        feature.SetGeometry(geojson_feature_geom)
        #add feature to layer
        shp_layer.CreateFeature(feature)
