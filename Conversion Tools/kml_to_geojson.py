#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/kml_to_geojson.py
Description:   This code converts kml data format to geojson format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

#a kml example file
kml_file = "../static_files/kml/Google_Campus.kmz"

#open the kml file
kml_datasource = ogr.Open(kml_file)

#get number of layers in kml file
layer_number = kml_datasource.GetLayerCount()
for each in range(layer_number):
    #get layer from kml file
    layer = kml_datasource.GetLayerByIndex(each)
    #get number of features from kml layer
    features_number = layer.GetFeatureCount()
    for i in range(features_number):
        #get one feature from kml layer
        feature = layer.GetFeature(i + 1)
        #get the feature geometry and convert to GeoJSON format
        print feature.GetGeometryRef().ExportToJson()
