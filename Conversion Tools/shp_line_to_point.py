#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_line_to_point.py
Description:   This code converts polygon shapfile to point shapefile.
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

#an example of shapefile data
line_shp_file = "../static_files/shapefile/rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp"

#open line shapefile
line_datasource = ogr.Open(line_shp_file)

#set driver to shapefile to be able to create point shapefile file
driver = ogr.GetDriverByName('ESRI Shapefile')

#output point shapefile file name
point_shp_file = 'points.shp'

#output point shapefile file layer name
layer_name = 'point_layer'

#create shapefile data_source(file)
if os.path.exists(point_shp_file):
    driver.DeleteDataSource(point_shp_file)
point_datasource = driver.CreateDataSource(point_shp_file)

#get number of layers of line shapefile
layer_count = line_datasource.GetLayerCount()
for each_layer in range(layer_count):
    #get one line shapefile
    layer = line_datasource.GetLayerByIndex(each_layer)

    #get line shapefile spatial reference
    srs = layer.GetSpatialRef()

    #create point shapefile layer with same spatial reference as line shapefile
    point_shp_layer = point_datasource.CreateLayer(layer_name, srs, ogr.wkbPoint)

    #get number of features of line shapefile
    feature_count = layer.GetFeatureCount()
    for each_feature in range(feature_count):
        #get each line feature
        line_feature = layer.GetFeature(each_feature)
        #get line feature geometry
        feature_geom = line_feature.GetGeometryRef()
        if feature_geom.GetGeometryName() != 'MULTILINESTRING':
            #get points data from each line feature
            points = feature_geom.GetPoints()
            for point in points:
                #make point geometry
                point_geom = ogr.Geometry(ogr.wkbPoint)
                #add point to point geometry
                point_geom.AddPoint(point[0], point[1])
                #define point feature
                point_feature = ogr.Feature(point_shp_layer.GetLayerDefn())
                #add point to point feature
                point_feature.SetGeometry(point_geom)
                #add point feature to poitn layer
                point_shp_layer.CreateFeature(point_feature)
