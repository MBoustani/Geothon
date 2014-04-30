#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_to_geojson.py
Description:   This code converts shapefile data format to geojson format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

try:
    import ogr
except ImportError:
    from osgeo import ogr

#an example shapefile file
shp_file = "../static_files/shapefile/watershed/huc18_250k.shp"

#open shapefile
shp_datasource = ogr.Open(shp_file)

#get number of layers in shapefile
layer_number = shp_datasource.GetLayerCount()

for each in range(layer_number):
    #get shapefile layer
    layer = shp_datasource.GetLayerByIndex(each)
    #get number of features in one shapefile layer
    features_number = layer.GetFeatureCount()
    for i in range(features_number):
        #get one shapefile feature
        feature = layer.GetFeature(i)
        #export feature geometry to GeoJSON format
        print feature.GetGeometryRef().ExportToJson()
