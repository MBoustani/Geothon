#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_to_kml.py
Description:   This code converts shapefile data format to kml format.
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

#an example shapefile file
shp_file = "../static_files/shapefile/rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp"

#open the shapefile
shp_datasource = ogr.Open(shp_file)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#set driver to KML to be able to create kml file
driver = ogr.GetDriverByName('KML')

#kml file to export
kml_file = 'line.kml'

#kml layer
layer_name = 'kml_layer'

#create a kml datasource
kml_datasource = driver.CreateDataSource(kml_file)

#create a kml layer for kml datasource
kml_layer = kml_datasource.CreateLayer(layer_name, srs, ogr.wkbLineString)

#get shapefile layer number
layer_number = shp_datasource.GetLayerCount()

for each in range(layer_number):
    #get shapefile layer
    layer = shp_datasource.GetLayerByIndex(each)
    #get number of features in shapefile layer
    features_number = layer.GetFeatureCount()
    for i in range(features_number):
        #get shapefile feature
        shp_feature = layer.GetFeature(i)
        #get shapefile feature geometry
        feature_geometry = shp_feature.GetGeometryRef()
        #define a kml feature
        kml_feature = ogr.Feature(kml_layer.GetLayerDefn())
        #set kml feature geometry
        kml_feature.SetGeometry(feature_geometry)
        #create kml feature in kml layer
        kml_layer.CreateFeature(kml_feature)
