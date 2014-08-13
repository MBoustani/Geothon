#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/geojson_to_wkt.py
Description:   This code converts geojson data format to wkt format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

json_file = "../static_files/geojson/test.json"

#read the geojson file
json_datasource = ogr.Open(json_file)

#get number of layer in geojson
layer_number = json_datasource.GetLayerCount()

for each in range(layer_number):
    #get geojson layer
    layer = json_datasource.GetLayerByIndex(each)
    #get number of features on geojson layer
    features_number = layer.GetFeatureCount()
    for i in range(features_number):
        #get feature from geojson layer
        feature = layer.GetFeature(i)
        #convert feature geometry to WKT
        print feature.GetGeometryRef().ExportToWkt()
