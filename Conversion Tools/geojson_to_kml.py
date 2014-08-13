#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/geojson_to_kml.py
Description:   This code converts geojson data format to kml format.
Author:        Maziyar Boustani (github.com/MBoustani)
'''

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

#set driver to KML to be able to create kml file
driver = ogr.GetDriverByName('KML')

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

        #create a new kml for each geometry(point, line and polygon)
        kml_file = 'kml_{0}.kml'.format(geojson_feature_name)
        #define a layer for each kml
        layer_name = 'kml_layer'

        #make kml datasource (file)
        kml_datasource = driver.CreateDataSource(kml_file)

        #create a kml layer for kml datasource
        kml_layer = kml_datasource.CreateLayer(layer_name, srs, geojson_feature_type)

        #define a feature for kml
        feature = ogr.Feature(kml_layer.GetLayerDefn())
        #add geometry from GeoJSON to kml feature
        feature.SetGeometry(geojson_feature_geom)
        #add feature to layer
        kml_layer.CreateFeature(feature)
