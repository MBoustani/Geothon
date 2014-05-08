#!/usr/bin/env python

'''
Project:       Geothon (https://github.com/MBoustani/Geothon)
File:          Conversion_Tools/shp_polygon_to_line.py
Description:   This code convert polygon shapfile to line shapfile data.
Author:        Maziyar Boustani (github.com/MBoustani)
'''
import os

try:
    import ogr
except ImportError:
    from osgeo import ogr

#an example of shapefile data
polygon_shp_file = "../static_files/shapefile/land_boundaries/land_boundaries.shp"

#open polygon shapefile
polygon_datasource = ogr.Open(polygon_shp_file)

#set driver to shapefile to be able to create line shapefile file
driver = ogr.GetDriverByName('ESRI Shapefile')

#output line shapefile file name
line_shp_file = 'lines.shp'

#output line shapefile file layer name
layer_name = 'line_layer'

#create line shapefile data_source(file)
if os.path.exists(line_shp_file):
    driver.DeleteDataSource(line_shp_file)
line_datasource = driver.CreateDataSource(line_shp_file)

#get number of layers of polygon shapefile
layer_count = polygon_datasource.GetLayerCount()
for layer in range(layer_count):
    #get layer of polygon shapefile
    layer = polygon_datasource.GetLayerByIndex(layer)
    #get spatial reference of polygon shapefile
    srs = layer.GetSpatialRef()

    #make layer for line shapefile
    layer_shp_layer = line_datasource.CreateLayer(layer_name, srs, ogr.wkbLineString)

    #get number of features of polygon shapefile
    feature_count = layer.GetFeatureCount()
    for each in range(feature_count):
        #get polygon feature
        polygon_feature = layer.GetFeature(each)
        #get polygon feauter's geometry
        feature_geom = polygon_feature.GetGeometryRef()

        for geom in feature_geom:
            #if the geometry type of polygon feature is linearring
            #then get the points
            gtype = geom.GetGeometryName()
            if gtype == "LINEARRING":
                points = geom.GetPoints()
            #if the geometry type is polygon, get the linearring
            #   geometry and then get points
            else:
                points = geom.GetGeometryRef(0).GetPoints()
            #define a line geometry
            line = ogr.Geometry(ogr.wkbLineString)
            for point in points:
                #add points to line geometry
                line.AddPoint(point[0], point[1])
            #define a line feature
            line_feature = ogr.Feature(layer_shp_layer.GetLayerDefn())
            #add point to line feature
            line_feature.SetGeometry(line)
            #add line feature to line layer
            layer_shp_layer.CreateFeature(line_feature)
