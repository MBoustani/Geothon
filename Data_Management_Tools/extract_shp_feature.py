#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/extract_shp_feature.py
Description:   This code extracts some features from shapefile features and create a new shapefile
               from extracted features.
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

#an example input shapefile file
in_shp = '../static_files/shapefile/rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp'

#open input shapefile
in_shp_datasource = ogr.Open(in_shp)

#create spatial reference
srs = osr.SpatialReference()
#in this case wgs84
srs.ImportFromEPSG(4326)

#output shapefile name
out_shp = 'extracted_feature.shp'
#output shapefile layer
out_layer_name = 'layer'

#create ESRI shapefile dirver
driver = ogr.GetDriverByName('ESRI Shapefile')

#create shapefile data_source(file)
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)
out_shp_datasource = driver.CreateDataSource(out_shp)

#create shapefile layer as line data with wgs84 as spatial reference
out_layer = out_shp_datasource.CreateLayer(out_layer_name, srs, ogr.wkbLineString)

#get input shapefile layer number
layer_number = in_shp_datasource.GetLayerCount()

#get input shapefile layer
in_layer = in_shp_datasource.GetLayerByIndex(0)

#get input shapefile layer definition
in_layer_defn = in_layer.GetLayerDefn()
#get input shapefile number of field
num_field_col = in_layer_defn.GetFieldCount()

#copy attribute fileds from input to output shapefile
for each in range(num_field_col):
    field = in_layer_defn.GetFieldDefn(each)
    out_layer.CreateField(field)

#get number of features in shapefile layer
features_number = in_layer.GetFeatureCount()
for i in range(features_number):
    #get input shapefile feature
    in_shp_feature = in_layer.GetFeature(i)
    #get input shapefile feature geometry
    in_feature_geometry = in_shp_feature.GetGeometryRef()
    #get the feature lenght (line lenght)
    in_feature_length = in_feature_geometry.Length()
    #select features with lenght more thatn 20
    if in_feature_length > 20:
        #create a new feature on output shapefile
        out_layer.CreateFeature(in_shp_feature)
