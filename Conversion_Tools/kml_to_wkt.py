#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/kml_to_wkt.py
Description:   This code converts kml data format to wkt format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

#an example KML file
kml_file = "../static_files/kml/Google_Campus.kmz"

#read the kml file
kml_datasource = ogr.Open(kml_file)

#get number of layers in kml file
layer_number = kml_datasource.GetLayerCount()
for each in range(layer_number):
    #get layer from kml file
    layer = kml_datasource.GetLayerByIndex(each)
    #get number of features in one kml layer
    features_number = layer.GetFeatureCount()
    for i in range(features_number):
        #get feature from kml layer
        feature = layer.GetFeature(i + 1)
        #get feature geometry and convert to WKT format
        print feature.GetGeometryRef().ExportToWkt()
